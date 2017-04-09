#!/usr/bin/python3
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.logger import ConsoleLogger
from bitz.util import update_fixtime


class ExchBacktesting(object):
    """
    Exchange gateway server
    """
    def __init__(self, name, market_data_feed, network_latency=200):
        """
        Constructo
        :param name: Exchange name
        :param market_data_feed: Market data feed
        :param network_latency: The network latency on messages
        """
        self.__name = name
        self.__market_data_feed = market_data_feed
        self.__network_latency = network_latency
        self.__exch_order_id = 0
        self.__open_positions = {}

    def get_name(self):
        """
        Get the exchange name
        """
        return self.__name

    def __get_next_exch_order_id(self):
        """
        Get the next exchange order id
        :return: Exchange order id, an integer
        """
        self.__exch_order_id += 1
        return self.__exch_order_id

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
            if True:
                fix_response = self.__prepare_exectype_new(req)
            # else:
            #     # Ignore the case of rejection first
            #     fix_response.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
            #     fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
            #     fix_response.OrdRejReason.value = Fix.Tags.OrdRejReason.Values.OTHER
            #     fix_response.Text.value = "Rejected by the exchange."

            # Add TransactTime
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag)
            # Ready to send
            fix_responses.append(fix_response)
            self.__open_positions[fix_response.OrderID.value] = [fix_response]

        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            if req.OrderID.value not in self.__open_positions.keys():
                # Reject with order not found
                pass
            elif self.__open_positions[req.OrderID.value][-1].LeavesQty.value == 0:
                # Reject completed order
                pass
            else:
                fix_response = self.__prepare_exectype_canceled(req)
            # else:
            #     fix_response = Fix.Messages.OrderCancelReject()
            #     fix_response.ClOrdID.value = req.ClOrdID.value
            #     fix_response.OrderID.value = req.OrderID.value
            #     fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
            #     fix_response.CxlRejResponseTo.value = Fix.Tags.CxlRejResponseTo.Values.ORDER_CANCEL_REQUEST
            #     fix_response.Text.value = self.get_failed_msg(response)
            #     fix_response.CxlRejReason.value = Fix.Tags.CxlRejReason.Values.OTHER
            #     if 'responseStatus' in response and \
            #        'errorCode' in response['responseStatus']:
            #         fix_response.CxlRejReason.value = response['responseStatus']['errorCode']

            # Add TransactTime
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag)
            # Ready to send
            fix_responses.append(fix_response)

        elif msgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            response = self.request_order_mass_status_request(req)

            if self.eig.check_success(response):
                fix_responses = self.parse_orders_get_result(response)
            else:
                err_msg = self.get_failed_msg(response)
        elif msgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            response = self.request_positions(req)

            if self.eig.check_success(response):
                fix_response = self.parse_balances_result(response)
                fix_responses.append(fix_response)
            else:
                assert False, "Not yet implemented %s" % msgType
        else:
            assert False, "MsgType (%s) has not yet been implemented." % msgType

        return fix_responses, err_msg

    def __prepare_execution_report(self, req):
        """
        Prepare an execution report
        :param req: Order request
        :return: Execution report
        """
        response = Fix.Messages.ExecutionReport()
        response.Instrument.Symbol.value = req.Instrument.Symbol.value
        response.Instrument.SecurityExchange.value = req.Instrument.SecurityExchange.value
        response.ClOrdID.value = req.ClOrdID.value
        response.Side.value = req.Side.value
        return response

    def __prepare_exectype_new(self, req):
        """
        Prepare an execution report with ExecType = NEW
        :param req: Order request
        :return: Execution report
        """
        response = self.__prepare_execution_report(req)
        response.OrderID.value = self.__get_next_exch_order_id()
        response.ExecType.value = Fix.Tags.ExecType.Values.NEW
        response.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
        response.Price.value = req.Price.value
        response.OrdType.value = req.OrdType.value
        response.TimeInForce.value = req.TimeInForce.value
        response.OrderQtyData.OrderQty.value = req.OrderQtyData.OrderQty.value
        response.ExecType.value = Fix.Tags.ExecType.Values.NEW
        response.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
        response.LeavesQty.value = response.OrderQtyData.OrderQty.value
        response.LastQty.value = 0
        response.CumQty.value = 0
        response.LastPx.value = 0
        return response

    def __prepare_exectype_canceled(self, req):
        """
        Prepare an execution report with ExecType = NEW
        :param req: Order request
        :return: Execution report
        """
        assert req.OrderID.value in self.__open_positions.keys()
        open_position = self.__open_positions[req.OrderID.value]

        response = self.__prepare_execution_report(req)
        response.OrderID.value = req.OrderID.value
        response.ExecType.value = Fix.Tags.ExecType.Values.CANCELED
        response.OrdStatus.value = Fix.Tags.OrdStatus.Values.CANCELED
        response.Price.value = open_position[-1].Price.value
        response.OrdType.value = open_position[-1].OrdType.value
        response.TimeInForce.value = open_position[-1].TimeInForce.value
        response.OrderQtyData.OrderQty.value = open_position[-1].OrderQtyData.OrderQty.value
        response.LeavesQty.value = 0
        response.LastQty.value = open_position[-1].LastQty.value
        response.CumQty.value = open_position[-1].CumQty.value
        response.LastPx.value = open_position[-1].LastPx.value
        return response
