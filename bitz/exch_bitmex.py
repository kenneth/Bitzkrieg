#!/bin/python
from bitz.rest_api_connector import RestApiConnector
from bitz.logger import ConsoleLogger
from bitz.exchange import Exchange
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.fix_message_factory import FixMessageFactory
from bitz.util import fixmsg2dict
import hashlib
import hmac
from requests import auth
from urllib.parse import urlparse
from uuid import uuid4 as uuid
import json

class ExchBitmexRestApiConnector(RestApiConnector):
    """
    Exchange BitMEX
    """
    URL = 'https://www.bitmex.com/api/v1/'

    def __init__(self, logger, public_key, private_key):
        """
        Constructor
        """
        RestApiConnector.__init__(self,
                                  logger,
                                  public_key,
                                  private_key,
                                  ExchBitmexRestApiConnector.URL)

    @classmethod
    def generate_signature(cls, secret, verb, url, nonce, data):
        """Generate a request signature compatible with BitMEX."""
        # Parse the url so we can remove the base and extract just the path.
        parsedURL = urlparse(url)
        path = parsedURL.path
        if parsedURL.query:
            path = path + '?' + parsedURL.query

        # print "Computing HMAC: %s" % verb + path + str(nonce) + data
        message = verb + path + str(nonce) + data

        signature = hmac.new(bytes(secret, 'utf8'), bytes(message, 'utf8'), digestmod=hashlib.sha256).hexdigest()
        return signature

    class APIKeyAuth(auth.AuthBase):
        """Attaches API Key Authentication to the given Request object."""

        def __init__(self, apiKey, apiSecret):
            """Init with Key & Secret."""
            self.apiKey = apiKey
            self.apiSecret = apiSecret

        def __call__(self, r):
            """Called when forming a request - generates api key headers."""
            # modify and return the request
            nonce = ExchBitmexRestApiConnector.generate_nonce()
            r.headers['api-nonce'] = str(nonce)
            r.headers['api-key'] = self.apiKey
            r.headers['api-signature'] = ExchBitmexRestApiConnector.generate_signature(
                                        self.apiSecret, r.method, r.url, nonce, r.body or '')
            return r

    def generate_auth(self):
        """
        Generate authentication
        """
        return ExchBitmexRestApiConnector.APIKeyAuth(self._public_key, self._private_key)

    def generate_headers(self, params):
        """
        Generate headers
        """
        return {'user-agent': 'liquidbot-1.0',
                  'content-type': 'application/json',
                  'accept': 'application/json' }

    def format_data(self, params):
        """
        Format the data to exchange desirable format
        """
        return json.dumps(params)

class ExchBitmex(Exchange):
    """
    Exchange BitMEX
    """
    def __init__(self, logger, public_key, private_key):
        Exchange.__init__(self)
        self.api_connector = ExchBitmexRestApiConnector(logger, public_key, private_key)

    @classmethod
    def get_name(cls):
        """
        Get name
        """
        return 'BitMEX'

    @classmethod
    def parse_timeinforce(cls, timeinforce_string):
        """
        Parse TimeInForce value
        """
        if timeinforce_string == "GoodTillCancel":
            return Fix.Tags.TimeInForce.Values.GOOD_TILL_CANCEL
        elif timeinforce_string == "ImmediateOrCancel":
            return Fix.Tags.TimeInForce.Values.IMMEDIATE_OR_CANCEL
        elif timeinforce_string == "FillOrKill":
            return Fix.Tags.TimeInForce.Values.FILL_OR_KILL
        else:
            raise NotImplementedError("TimeInForce value (%s) cannot be recognized." % timeinforce_string)

    def request(self, req):
        """
        Request
        """
        msgType = req.MsgType
        fix_responses = []
        err_msg = ""

        if msgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            ##############################################################################################
            # Order placement
            ##############################################################################################
            response = self.request_new_order_single(req)
            if response is None:
                err_msg = "No response from the exchange connector"
            elif response.status_code == 200:
                # Success
                response = response.json()
                fix_response = FixMessageFactory.create_execution_report_from_new_order_single(req, response["orderID"])
                fix_responses.append(fix_response)
            else:
                # Failed
                fix_response = FixMessageFactory.create_execution_report_reject_from_new_order_single(
                                req,
                                Fix.Tags.OrdRejReason.Values.OTHER,
                                "Http error (%d): %s" % (response.status_code, response.text))
                fix_responses.append(fix_response)
        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            ##############################################################################################
            # Order cancellation
            ##############################################################################################
            response = self.request_order_cancel_request(req)
            if response is None:
                err_msg = "No response from the exchange connector"
            elif response.status_code == 200:
                # Success
                fix_response = FixMessageFactory.create_execution_report(
                                exchange=req.Instrument.SecurityExchange.value,
                                symbol=req.Instrument.Symbol.value,
                                orderid=req.OrderID.value,
                                clordid=req.ClOrdID.value,
                                exectype=Fix.Tags.ExecType.Values.CANCELED,
                                ordstatus=Fix.Tags.OrdStatus.Values.CANCELED,
                                leavesqty=0)
                fix_responses.append(fix_response)
            else:
                # Failed
                fix_response = FixMessageFactory.create_order_cancel_reject(
                                orderid=req.OrderID.value,
                                clordid=req.ClOrdID.value,
                                cancelrejtext=response.text)
                fix_responses.append(fix_response)
        elif msgType == Fix.Tags.MsgType.Values.ORDERMASSCANCELREQUEST:
            ##############################################################################################
            # Order mass cancel
            ##############################################################################################
            response = self.request_order_mass_cancel_request(req)
            if response is None:
                err_msg = "No response from the exchange connector"
            elif response.status_code == 200:
                # Success
                fix_response = FixMessageFactory.create_order_mass_cancel_report(req)
                fix_responses.append(fix_response)
            else:
                # Failed
                fix_response = FixMessageFactory.create_order_mass_cancel_report(req, Fix.Tags.MassCancelResponse.Values.CANCEL_REQUEST_REJECTED)
                fix_responses.append(fix_response)
        elif msgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST:
            ##############################################################################################
            # Order status request
            ##############################################################################################
            response = self.request_order_status_request(req)
            if response is None:
                err_msg = "No response from the exchange connector"
            elif response.status_code == 200:
                # Success
                response = response.json()
                assert len(response)==1, "More than one responses (%d) is received." % len(response)
                response = response[0]
                fix_response = FixMessageFactory.create_execution_report(
                    symbol=req.Instrument.Symbol.value,
                    exchange=req.Instrument.SecurityExchange.value,
                    orderid=req.OrderID.value,
                    clordid=response["clOrdID"],
                    side=Fix.Tags.Side.Values.BUY if response["side"] == "Buy" else Fix.Tags.Side.Values.SELL,
                    price=response["price"],
                    qty=response["orderQty"],
                    ordtype=Fix.Tags.OrdType.Values.LIMIT if response["ordType"] == "Limit" else Fix.Tags.OrdType.Values.MARKET,
                    leavesqty=response["leavesQty"],
                    cumqty=response["cumQty"],
                    avgpx=response["avgPx"],
                    transacttime=response["transactTime"].replace("-", "").replace("Z", "") + "000",
                    timeinforce=self.parse_timeinforce(response["timeInForce"]),
                    text=response["text"])
                fix_response.OrdStatusReqID.value = req.OrdStatusReqID.value
                fix_responses.append(fix_response)
            else:
                # Failed
                err_msg = "Request is rejected."
        elif msgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            ##############################################################################################
            # Order mass status request
            ##############################################################################################
            response = self.request_order_mass_status_request(req)
            if response is None:
                err_msg = "No response from the exchange connector"
            elif response.status_code == 200:
                # Success
                response = response.json()
                for position in response:
                    fix_response = FixMessageFactory.create_execution_report(
                        symbol=position["symbol"],
                        exchange=self.get_name(),
                        orderid=position["orderID"],
                        clordid=position["clOrdID"],
                        side=Fix.Tags.Side.Values.BUY if position["side"] == "Buy" else Fix.Tags.Side.Values.SELL,
                        price=position["price"],
                        qty=position["orderQty"],
                        ordtype=Fix.Tags.OrdType.Values.LIMIT if position["ordType"] == "Limit" else Fix.Tags.OrdType.Values.MARKET,
                        leavesqty=position["leavesQty"],
                        cumqty=position["cumQty"],
                        avgpx=position["avgPx"],
                        transacttime=position["transactTime"].replace("-", "").replace("Z", "") + "000",
                        timeinforce=self.parse_timeinforce(position["timeInForce"]),
                        text=position["text"])
                    fix_response.OrdStatusReqID.value = req.MassStatusReqID.value
                    fix_responses.append(fix_response)
            else:
                # Failed
                err_msg = "Request is rejected."

        elif msgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            ##############################################################################################
            # Request for positions
            ##############################################################################################
            response = self.request_for_position(req)
            if response is None:
                err_msg = "No response from the exchange connector"
            elif response.status_code == 200:
                response = response.json()
                fix_response = self.handle_positions(req, response)
                fix_responses.append(fix_response)
            else:
                # Failed
                err_msg = "Request is rejected."
        else:
            ##############################################################################################
            # Default behavior
            ##############################################################################################
            assert False, "MsgType (%s) has not yet been implemented." % msgType

        return fix_responses, err_msg

    def request_new_order_single(self, req: Fix.Messages.NewOrderSingle):
        """
        Handle NewOrderSingle request
        :param req Reuest
        :return Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE, \
            "Order request is not NEWORDERSINGLE"
        symbol = req.Instrument.Symbol.value
        ordType = req.OrdType.value
        orderQty = req.OrderQtyData.OrderQty.value
        side = req.Side.value
        if ordType == Fix.Tags.OrdType.Values.LIMIT:
            price = req.Price.value
            ordType = "Limit"
        elif ordType == Fix.Tags.OrdType.Values.MARKET:
            price = 0
            ordType = "Limit"
        else:
            raise NotImplementedError("OrdType (%s) has not yet implemented." % ordType)

        params = { "symbol": symbol,
                   "ordType": ordType,
                   "side": 'Buy' if side == Fix.Tags.Side.Values.BUY else 'Sell',
                   "orderQty": orderQty,
                   "price": price,
                   "clOrdID": req.ClOrdID.value
                   }

        return self.api_connector.send_request("Order", RestApiConnector.HTTPMethod.POST, params)

    def request_order_cancel_request(self, req):
        """
        Handle OrderCancelRequest request
        :param req Reuest
        :return Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST, \
            "Order request is not ORDERCANCELREQUEST"
        orderID = req.OrderID.value
        params = { "orderID": orderID }
        return self.api_connector.send_request("Order", RestApiConnector.HTTPMethod.DELETE, params)

    def request_order_mass_cancel_request(self, req):
        """
        Request OrderMassCancelRequest
        :param req: Request
        :return: Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERMASSCANCELREQUEST, \
            "Order request is not ORDERMASSCANCELREQUEST"
        return self.api_connector.send_request("Order/all", RestApiConnector.HTTPMethod.DELETE, None)

    def request_order_mass_status_request(self, req):
        """
        Send order status request
        :param req: Request
        :return: Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST, \
            "Order request is not ORDERMASSSTATUSREQUEST"

        return self.api_connector.send_request("Order", RestApiConnector.HTTPMethod.GET, None)

    def request_order_status_request(self, req):
        """
        Send order status request
        :param req: Request
        :return: Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST, \
            "Order request is not ORDERSTATUSREQUEST"

        params = { "filter": "{\"orderID\": \"%s\"}" % req.OrderID.value }
        return self.api_connector.send_request("Order", RestApiConnector.HTTPMethod.GET, params)

    def request_for_position(self, req):
        """
        Send request for position
        :param req: Request
        :return: Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS, \
            "Order request is not REQUESTFORPOSITIONS"

        params = { "currency": "all" }
        return self.api_connector.send_request("user/margin", RestApiConnector.HTTPMethod.GET, params)

    def handle_positions(self, req: Fix.Messages.RequestForPositions, response):
        """
        Handle position replied from the exchange
        :param req: Request for position
        :param response: Exchange response in a list of dictionaries
        :return: PositionReport report
        """
        report = FixMessageFactory.create_position_report(exchange=self.get_name(),
                                                          reqid=req.PosReqID.value,
                                                          posid=str(uuid()),
                                                          account=self.api_connector.get_public_key())
        for margin in response:
            report.PositionAmountData.groups.append(FixMessageFactory.create_position_amount_data(
                currency=margin["currency"],
                amount=margin["amount"],
                type=Fix.Tags.PosAmtType.Values.CASH_AMOUNT))
            report.PositionAmountData.groups.append(FixMessageFactory.create_position_amount_data(
                currency=margin["currency"],
                amount=margin["availableMargin"],
                type=Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT))
        return report


if __name__ == '__main__':
    public = 'your_public_key'
    private = 'your_private_key'
    exch = ExchBitmex(ConsoleLogger.static_logger, public, private)
    req = FixMessageFactory.create_new_single_order(exchange='BitMEX',
                                                    symbol='XBTUSD',
                                                    side=Fix.Tags.Side.Values.BUY,
                                                    price=2000,
                                                    qty=10,
                                                    clordid=str(uuid()))
    report, err_msg = exch.request(req)
    print(fixmsg2dict(report[0]))
    req = FixMessageFactory.create_order_status_request(exchange='BitMEX',
                                                        symbol='XBTUSD',
                                                        orderid=report[0].OrderID.value,
                                                        reqId=str(uuid()))
    status_report, err_msg = exch.request(req)
    print(fixmsg2dict(status_report[0]))
    req = FixMessageFactory.create_order_cancel_request(exchange='BitMEX',
                                                        symbol='XBTUSD',
                                                        orderid=report[0].OrderID.value,
                                                        clordid=str(uuid()))
    report, err_msg = exch.request(req)
    print(fixmsg2dict(report[0]))
    # req = FixMessageFactory.create_request_for_position(reqid=str(uuid()))
    # report, err_msg = exch.request(req)
    # assert len(report) == 1, "Number of reports is not one."
    # print(fixmsg2dict(report[0]))


