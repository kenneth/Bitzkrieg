#!/usr/bin/python3
from bitz.exchange import Exchange
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.exch_gatecoin_eig import ExchGatecoinEig
from bitz.logger import ConsoleLogger
from bitz.util import update_fixtime
from datetime import datetime
from uuid import uuid4 as uuid
import argparse
import json
import sys

class ExchGatecoinEis(Exchange):
    """
    Exchange gateway server
    """
    def __init__(self, eig):
        Exchange.__init__(self)
        self.eig = eig

    @staticmethod
    def __create_unique_id():
        return datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f") + '-' + str(uuid())

    @classmethod
    def get_name(cls):
        """
        Get name
        :return: Name
        """
        return 'Gatecoin'

    def generate_execution_report(self):
        """
        Generate execution report
        """
        fix_message = Fix.Messages.ExecutionReport()
        return fix_message

    def request(self, req):
        """
        Handle a request
        :param req              FIX message
        :return True if the request is successful.
        """
        msgType = req.MsgType
        fix_responses = []
        err_msg = ""

        if msgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            response = self.request_new_order_single(req)

            fix_response = self.generate_execution_report()
            fix_response.Instrument.Symbol.value = req.Instrument.Symbol.value
            fix_response.Instrument.SecurityExchange.value = req.Instrument.SecurityExchange.value
            if self.eig.check_success(response):
                fix_response.OrderID.value = response['clOrderId']
                fix_response.ExecType.value = Fix.Tags.ExecType.Values.NEW
                fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
                fix_response.OrderQtyData.OrderQty.value = req.OrderQtyData.OrderQty.value
                fix_response.Side.value = req.Side.value
                fix_response.Price.value = req.Price.value
                fix_response.ClOrdID.value = req.ClOrdID.value
                fix_response.OrdType.value = req.OrdType.value
                fix_response.CumQty.value = 0
                fix_response.LeavesQty.value = fix_response.OrderQtyData.OrderQty.value
            else:
                fix_response.ClOrdID.value = req.ClOrdID.value
                fix_response.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
                fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
                fix_response.OrdRejReason.value = Fix.Tags.OrdRejReason.Values.OTHER
                if 'responseStatus' in response and \
                   'message' in response['responseStatus'] and \
                   'errorCode' in response['responseStatus']:
                    err_msg = response['responseStatus']['message']
                    err_code = response['responseStatus']['errorCode']
                    fix_response.Text.value = err_msg
                    if int(err_code) >= 100:
                        fix_response.OrdRejReason.value = int(err_code)
                else:
                    fix_response.Text.value = "Rejected by the exchange."

            # Add TransactTime
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag)
            # Ready to send
            fix_responses.append(fix_response)

        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            response = self.request_order_cancel_request(req)

            if self.eig.check_success(response):
                fix_response = self.generate_execution_report()
                fix_response.Instrument.Symbol.value = req.Instrument.Symbol.value
                fix_response.Instrument.SecurityExchange.value = req.Instrument.SecurityExchange.value
                fix_response.ClOrdID.value = req.ClOrdID.value
                fix_response.OrderID.value = req.OrderID.value
                fix_response.ExecType.value = Fix.Tags.ExecType.Values.CANCELED
                fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.CANCELED
                fix_response.LeavesQty.value = 0
            else:
                fix_response = Fix.Messages.OrderCancelReject()
                fix_response.ClOrdID.value = req.ClOrdID.value
                fix_response.OrderID.value = req.OrderID.value
                fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
                fix_response.CxlRejResponseTo.value = Fix.Tags.CxlRejResponseTo.Values.ORDER_CANCEL_REQUEST
                fix_response.Text.value = self.get_failed_msg(response)
                fix_response.CxlRejReason.value = Fix.Tags.CxlRejReason.Values.OTHER
                if 'responseStatus' in response and \
                   'errorCode' in response['responseStatus']:
                    fix_response.CxlRejReason.value = response['responseStatus']['errorCode']

            # Add TransactTime
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag)
            # Ready to send
            fix_responses.append(fix_response)

        elif msgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            response = self.request_order_mass_status_request(req)

            if self.eig.check_success(response):
                fix_responses = self.parse_orders_get_result(req, response)
            else:
                err_msg = self.get_failed_msg(response)
        elif msgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST:
            response = self.request_order_status_request(req)

            if self.eig.check_success(response):
                fix_responses = self.parse_orders_get_result(req, response)
            else:
                err_msg = self.get_failed_msg(response)
        elif msgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            response = self.request_positions(req)

            if self.eig.check_success(response):
                fix_response = self.parse_balances_result(req, response)
                fix_responses.append(fix_response)
            else:
                assert False, "Not yet implemented %s" % msgType
        else:
            assert False, "MsgType (%s) has not yet been implemented." % msgType

        return fix_responses, err_msg

    @classmethod
    def get_failed_msg(cls, response):
        err_msg = ''
        if 'failed_code' in response:
            err_msg += "(%d) " % response['failed_code']

        if 'failed_text' in response:
            err_msg += "%s " % response['failed_text']

        return err_msg

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
        side = req.Side.value
        if ordType == Fix.Tags.OrdType.Values.LIMIT:
            price = req.Price.value
        else:
            price = 0

        params = { "Code": symbol,
                    "Way": 'Bid' if side == Fix.Tags.Side.Values.BUY else 'Ask',
                    "Amount": orderQty,
                    "Price": price
                }

        return self.eig.send_request("Trade/Orders", "POST", params)

    def request_order_cancel_request(self, req):
        """
        Handle OrderCancelRequest request
        :param req Reuest
        :return Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST, \
             "Order request is not ORDERCANCELREQUEST"
        orderID = req.OrderID.value
        params = { "clOrderId": orderID }

        return self.eig.send_request("Trade/Orders/%s" % orderID, "DELETE", params)

    def request_positions(self, req):
        """
        Handle RequestForPositions
        :param req Reuest
        :return Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS, \
             "Order request is not REQUESTFORPOSITIONS"

        return self.eig.send_request("Balance/Balances", "GET", {})

    def request_order_mass_status_request(self, req):
        """
        Handle OrderMassStatusRequest
        :param req Reuest
        :return Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST, \
             "Order request is not ORDERMASSSTATUSREQUEST"

        return self.eig.send_request("Trade/Orders", "GET")

    def request_order_status_request(self, req):
        """
        Send order status request
        :param req: Request
        :return: Exchange response
        """
        assert req.MsgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST, \
            "Order request is not ORDERSTATUSREQUEST"

        param = { "clOrderId" : req.OrderID.value }
        return self.eig.send_request("Trade/Orders/%s" % req.OrderID.value, "GET", param)

    def parse_orders_get_result(self, req, response):
        """
        Parsing "GET Trade/Orders" response
        :param response Response from exchange
        :result Fix message

        """
        assert "orders" in response.keys() or "order" in response.keys()
        orders = response["orders"] if "orders" in response.keys() else [response["order"]]
        fix_messages = []
        for order in orders:
            leavesQty = order["remainingQuantity"]
            orderID = order["clOrderId"]
            side = order["side"]
            orderQty = order["initialQuantity"]
            ordStatus = order["status"]
            ordType = order["type"]
            price = order["price"]
            fix_message = self.generate_execution_report()
            fix_message.Instrument.Symbol.value = req.Instrument.Symbol.value
            fix_message.Instrument.SecurityExchange.value = req.Instrument.SecurityExchange.value
            fix_message.OrderID.value = req.OrderID.value if req.MsgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST \
                                        else orderID
            fix_message.Side.value = Fix.Tags.Side.Values.BUY if side == 0 \
                                    else Fix.Tags.Side.Values.SELL
            fix_message.OrderQtyData.OrderQty.value = orderQty
            fix_message.LeavesQty.value = leavesQty
            fix_message.CumQty.value = orderQty - leavesQty
            fix_message.Price.value = price
            if ordStatus == 1:
                fix_message.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
            elif ordStatus == 6:
                fix_message.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                fix_message.AvgPx.value = fix_message.Price.value
            else:
                fix_message.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED if leavesQty == 0 \
                                                else Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                fix_message.AvgPx.value = fix_message.Price.value
            fix_message.ExecType.value = Fix.Tags.ExecType.Values.ORDER_STATUS;
            fix_message.OrdType.value = Fix.Tags.OrdType.Values.MARKET if ordType == 1 \
                                        else Fix.Tags.OrdType.Values.LIMIT
            if fix_message.OrdType.value != Fix.Tags.OrdType.Values.MARKET:
                fix_message.Price.value = price

            fix_messages.append(fix_message)

        return fix_messages

    def parse_balances_result(self, req, balances):
        """
        Parsing "GET Balance/Balances" response
        :param response Response from exchange
        :result Fix message
        """
        assert "balances" in balances.keys()
        balances = balances["balances"]
        fix_message = Fix.Messages.PositionReport()
        fix_message.PosReqID.value = req.PosReqID.value
        fix_message.PosMaintRptID.value = ExchGatecoinEis.__create_unique_id()
        fix_message.Instrument.SecurityExchange.value = self.get_name()
        fix_message.ClearingBusinessDate.value = datetime.utcnow().strftime("%Y%m%d")
        fix_message.Account.value = self.eig.key
        for balance in balances:
            currency = balance["currency"]
            total_balance = balance["balance"]
            available_balance = balance["availableBalance"]

            # Total
            positionAmountData = Fix.Components.PositionAmountData.NoPosAmt()
            positionAmountData.PositionCurrency.value = currency
            positionAmountData.PosAmt.value = total_balance
            positionAmountData.PosAmtType.value = Fix.Tags.PosAmtType.Values.CASH_AMOUNT
            fix_message.PositionAmountData.groups.append(positionAmountData)

            # Available
            positionAmountData = Fix.Components.PositionAmountData.NoPosAmt()
            positionAmountData.PositionCurrency.value = currency
            positionAmountData.PosAmt.value = available_balance
            positionAmountData.PosAmtType.value = Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT
            fix_message.PositionAmountData.groups.append(positionAmountData)

        return fix_message

###############################################################################
# main
###############################################################################
def main():
    parser = argparse.ArgumentParser(description='Exchange gateway Gatecoin')
    parser.add_argument('-public', action='store', dest='public',
                        help='Your public API key.',
                        default='')
    parser.add_argument('-private', action='store', dest='private',
                        help='Your private API key.',
                        default='')
    parser.add_argument('-balance', action='store_true', help='Inquire account balance')
    parser.add_argument('-orders', action='store_true', help='Inquire account balance')
    parser.add_argument('-cancel', action='store_true', help='Cancel all outstanding orders')
    args = parser.parse_args()

    eig = ExchGatecoinEig(ConsoleLogger.static_logger, args.public, args.private)
    eis = ExchGatecoinEis(eig)
    logger = ConsoleLogger.static_logger

    if args.balance:
        logger.info('main', "Request for positions...")
        req = Fix.Messages.RequestForPositions()
        fix_responses, err_msg = eis.request(req)
        logger.info('main', 'Number of messages = %d' % len(fix_responses))
        ret = ''
        for pad in fix_responses[0].PositionAmountData.groups:
            ret += '%s[%s]:%.6f\n' % (pad.PositionCurrency.value, \
                                     pad.PosAmtType.value,
                                     pad.PosAmt.value)

        logger.info('main', ret)

    elif args.orders:
        logger.info('main', "Order mass status request...")
        req = Fix.Messages.OrderMassStatusRequest()
        fix_responses, err_msg = eis.request(req)
        logger.info('main', 'Number of messages = %d' % len(fix_responses))

        for fix_response in fix_responses:
            ConsoleLogger.static_logger.info('main', \
                ("Instrument = %s\n" % fix_response.Instrument.Symbol.value) +
                ("Order Id = %s\n" % fix_response.OrderID.value) +
                ("Order status = %s\n" % fix_response.OrdStatus.value) +
                ("Order price = %.6f\n" % fix_response.Price.value) +
                ("Order quantity = %.6f\n" % fix_response.OrderQtyData.OrderQty.value) +
                ("Cum quantity = %.6f\n" % fix_response.CumQty.value) +
                ("Leaves quantity = %.6f\n" % fix_response.LeavesQty.value) +
                ("Order type = %s\n" % fix_response.OrdType.value)
                )
    elif args.cancel:
        logger.info('main', "Mass order cancellation...")
        req = Fix.Messages.OrderCancelRequest()
        req.OrderID.value = '0'
        fix_responses, err_msg = eis.request(req)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
