from bitz.rest_api_connector import RestApiConnector
from bitz.logger import ConsoleLogger
from urllib.parse import urlparse
import hmac
import hashlib
import urllib
from bitz.FIX50SP2 import FIX50SP2 as Fix
from uuid import uuid4 as uuid
from bitz.fix_message_factory import FixMessageFactory
from bitz.exchange import Exchange
import requests
from bitz.util import fixmsg2dict


# reference : https://poloniex.com/support/api/

class ExchPoloniexRestApiConnector(RestApiConnector):
    """
    Exchange BitMEX
    """
    URL = 'https://poloniex.com/tradingApi'

    def __init__(self, logger, public_key, private_key):
        """
        Constructor
        """
        RestApiConnector.__init__(self,
                                  logger,
                                  public_key,
                                  private_key,
                                  ExchPoloniexRestApiConnector.URL)

    def generate_auth(self):
        """
        Generate authentication
        """
        return None

    def generate_headers(self, data):
        """
        Generate headers
        """
        signature = hmac.new(secret.encode(), urllib.parse.urlencode(data).encode(),
                             digestmod=hashlib.sha512).hexdigest()
        header = {
            'Key': key,
            'Sign': signature
        }

        return header

    def format_data(self, params):
        """
        Format the data to exchange desirable format
        """
        return params

class ExchPoloniex(object):
    """
    Exchange Poloniex
    """

    def __init__(self, logger, public_key, private_key):
        Exchange.__init__(self)
        self.api_connector = ExchPoloniexRestApiConnector(logger, public_key, private_key)

        """
        Constructor

        :param key          Public key
        :param secret       Private key
        :param api_url      API URL
        """
        self.logger = logger
        self.key = key
        self.secret = secret

    @classmethod
    def get_name(cls):
        """
        Get name
        :return: Name
        """
        return 'Poloniex'

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
                err_msg = response.get('error', '')
            else:
                err_msg = "Http error (%d): %s" % (response.status_code, response.text)

            if err_msg == '':
                fix_response = FixMessageFactory.create_execution_report_from_new_order_single(req,
                                                                                               response["orderNumber"])
                fix_responses.append(fix_response)
            else:
                # Failed
                fix_response = FixMessageFactory.create_execution_report_reject_from_new_order_single(
                    req,
                    Fix.Tags.OrdRejReason.Values.OTHER,
                    err_msg)
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
                response = response.json()
                err_msg = response.get('error', '')
            else:
                err_msg = "Http error (%d): %s" % (response.status_code, response.text)

            if err_msg == '':
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
                    cancelrejtext=err_msg)
                fix_responses.append(fix_response)

        elif msgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            ##############################################################################################
            # Order Mass Status Request
            ##############################################################################################
            response = self.request_order_mass_status_request()
            if response is None:
                err_msg = "No response from the exchange connector"
            elif response.status_code == 200:
                response = response.json()
                err_msg = response.get('error', '')
                if err_msg == '':
                    fix_messages = []
                    for currency in response:
                        for order in response[currency]:
                            orderID = order["orderNumber"]
                            side = order["type"]  # buy or sell
                            price = order["rate"]
                            orderQty = float(order["startingAmount"])
                            leavesQty = float(order["amount"])

                            fix_message = Fix.Messages.ExecutionReport()
                            fix_message.Instrument.Symbol.value = req.Instrument.Symbol.value
                            fix_message.Instrument.SecurityExchange.value = req.Instrument.SecurityExchange.value
                            fix_message.OrderID.value = req.OrderID.value if req.MsgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST \
                                else orderID
                            fix_message.Side.value = Fix.Tags.Side.Values.BUY if side == 'buy' \
                                else Fix.Tags.Side.Values.SELL
                            fix_message.OrderQtyData.OrderQty.value = orderQty
                            fix_message.LeavesQty.value = leavesQty
                            fix_message.CumQty.value = orderQty - leavesQty
                            fix_message.Price.value = price
                            if orderQty == leavesQty:
                                fix_message.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
                            else:
                                # fully filled orders do not show up in mass request though...
                                fix_message.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED if leavesQty == 0 \
                                    else Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                                fix_message.AvgPx.value = fix_message.Price.value
                            fix_message.ExecType.value = Fix.Tags.ExecType.Values.ORDER_STATUS;
                            # only limit order for poloniex
                            fix_message.OrdType.value = Fix.Tags.OrdType.Values.LIMIT

                            fix_responses.append(fix_message)
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
                err_msg = response.get('error', '')
                if err_msg == '':
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

    def send_request(self, data):
        """
        Handle using api connector to send request
        """
        return self.api_connector.send_request('', RestApiConnector.HTTPMethod.POST, data)

    # Poloniex support IOC, FOK, post only as well but not implemented here.
    def request_new_order_single(self, req):
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
        side = 'buy' if req.Side.value == Fix.Tags.Side.Values.BUY else 'sell'
        if ordType == Fix.Tags.OrdType.Values.LIMIT:
            price = req.Price.value
        else:
            NotImplementedError('Only support limit order.')

        params = {
            'command': side,
            "currencyPair": symbol,
            "amount": orderQty,
            "rate": price,
            'nonce': ExchPoloniexRestApiConnector.generate_nonce()
        }
        return self.send_request(params)

    def request_order_cancel_request(self, req):
        """
        Handle OrderCancelRequest request
        :param req Reuest
        :return Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST, \
            "Order request is not ORDERCANCELREQUEST"
        params = {"command": "cancelOrder", "orderNumber": req.OrderID.value,
                  'nonce': ExchPoloniexRestApiConnector.generate_nonce()}
        return self.send_request(params)

    # Poloniex supports filter by currency but we simply retrieve all for now
    def request_order_mass_status_request(self):
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST, \
            "Order request is not ORDERMASSSTATUSREQUEST"
        params = {'command': 'returnOpenOrders', 'currencyPair': 'all',
                  'nonce': ExchPoloniexRestApiConnector.generate_nonce()}
        return self.send_request(params)

    def request_for_position(self, req):
        """
        Send request for position
        :param req: Request
        :return: Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS, \
            "Order request is not REQUESTFORPOSITIONS"
        data = {'command': 'returnCompleteBalances', 'nonce': ExchPoloniexRestApiConnector.generate_nonce()}
        return self.send_request(data)

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
        for currency in response:
            report.PositionAmountData.groups.append(FixMessageFactory.create_position_amount_data(
                currency=currency,
                amount=float(response[currency]["available"]) + float(response[currency]["onOrders"]),
                type=Fix.Tags.PosAmtType.Values.CASH_AMOUNT))
            report.PositionAmountData.groups.append(FixMessageFactory.create_position_amount_data(
                currency=currency,
                amount=float(response[currency]["available"]),
                type=Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT))
        return report


if __name__ == '__main__':
    # Run "curl icanhazip.com" to get the outgoing IP before generating the key pair.

    key = input("What is the public key? ")
    secret = input("What is the private key? ")

    # setup
    exch = ExchPoloniex(ConsoleLogger.static_logger, key, secret)

    print('Checking Position...')
    req = FixMessageFactory.create_request_for_position(reqid=str(uuid()))
    report, err_msg = exch.request(req)

    # output position result
    for position in report[0].PositionAmountData.groups:
        currency = position.PositionCurrency.value.upper()
        value = position.PosAmt.value
        type = position.PosAmtType.value
        if currency == 'BTC':
            print('BTC ' + type + ' ' + str(value))
    print(err_msg)
    print(fixmsg2dict(report[0]))
    assert err_msg == ""

    print()
    print('Checking all open orders...')
    req = FixMessageFactory.create_order_mass_status_request(reqId=str(uuid()),
                                                             exchange='Poloniex')
    report, err_msg = exch.request(req)
    print(err_msg)
    for order in report:
        print(fixmsg2dict(order))

    # try placing order, with error
    print()
    print('Placing too small order (error)...')
    req = FixMessageFactory.create_new_single_order(exchange='Poloniex',
                                                    symbol='BTC_ETH',
                                                    side=Fix.Tags.Side.Values.BUY,
                                                    price=0.0001,
                                                    qty=0.0001,
                                                    clordid=str(uuid()))
    report, err_msg = exch.request(req)
    print(err_msg)
    assert err_msg, 'Http error (422): {"error":"Total must be at least 0.0001."}'
    print(fixmsg2dict(report[0]))

    print()
    print('Placing a far away buy order...')
    req = FixMessageFactory.create_new_single_order(exchange='Poloniex',
                                                    symbol='BTC_ETH',
                                                    side=Fix.Tags.Side.Values.BUY,
                                                    price=0.001,
                                                    qty=0.4,
                                                    clordid=str(uuid()))
    report, err_msg = exch.request(req)
    print(err_msg)
    print(fixmsg2dict(report[0]))
    assert err_msg == ""

    print()
    print('Cancelling of the far away buy order...')
    req = FixMessageFactory.create_order_cancel_request(exchange='Poloniex',
                                                        symbol='BTC_ETH',
                                                        orderid=report[0].OrderID.value,
                                                        clordid=str(uuid()))
    report, err_msg = exch.request(req)
    print(err_msg)
    print(fixmsg2dict(report[0]))
    assert err_msg == ""

    # try out other command
    if 1 == 1:
        print("Trying other commands")
        # returning only available balances, excluding on order
        params = {'command': 'returnAvailableAccountBalances',
                  'nonce': ExchPoloniexRestApiConnector.generate_nonce()}
        response = exch.send_request(params)
        print(response)
        print(response.json())

        # not sure what tradable balacne is...
        params = {'command': 'returnTradableBalances', 'nonce': ExchPoloniexRestApiConnector.generate_nonce()}
        response = exch.send_request(params)
        print(response)
        print(response.json())

        params = {'command': 'returnMarginAccountSummary', 'nonce': ExchPoloniexRestApiConnector.generate_nonce()}
        response = exch.send_request(params)
        print(response)
        print(response.json())
