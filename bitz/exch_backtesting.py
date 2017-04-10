#!/usr/bin/python3
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.logger import ConsoleLogger
from bitz.util import update_fixtime
from datetime import timedelta
from copy import deepcopy

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
        self.__price_gap_detection = 100

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
            exchange = req.Instrument.SecurityExchange.value
            instmt = req.Instrument.Symbol.value
            if (exchange, instmt) not in self.__market_data_feed.snapshots.keys():
                # Reject the order with invalid instrument
                pass
            else:
                fix_response = self.__prepare_exectype_new(req)
            # else:
            #     # Ignore the case of rejection first
            #     fix_response.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
            #     fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
            #     fix_response.OrdRejReason.value = Fix.Tags.OrdRejReason.Values.OTHER
            #     fix_response.Text.value = "Rejected by the exchange."

            # Add TransactTime
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag, self.__market_data_feed.now())
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

    def snapshot_updated(self, snapshot):
        """
        Snapshot updated
        :param snapshot: The instrument snapshot
        :return FIX message responses if provided.
        """
        responses = []
        exchange = snapshot.exchange
        instmt = snapshot.instmt

        # For each open position, update the order status if necessary
        for order_id, order_updates in self.__open_positions.items():
            last_order_update = order_updates[-1]
            if last_order_update.Instrument.SecurityExchange.value == exchange and \
               last_order_update.Instrument.Symbol.value == instmt:
                if snapshot.update_type == snapshot.UpdateType.ORDER_BOOK:
                    # Order book update
                    if last_order_update.Side.value == Fix.Tags.Side.Values.BUY:
                        # BUY
                        if last_order_update.Price.value >= snapshot.a1 and \
                            snapshot.a1 > 0.0:
                            # Execution if the opposite best price equals or exceeds the price
                            response = deepcopy(last_order_update)
                            # Last price
                            response.LastPx.value = snapshot.a1
                            # Last quantity
                            response.LastQty.value = snapshot.aq1
                            # Leaves quantity and status
                            if snapshot.aq1 >= response.LeavesQty.value:
                                response.LeavesQty.value = 0
                                response.CumQty.values = response.OrderQtyData.OrderQty.value
                                response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                                response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                            else:
                                response.LeavesQty.value -= snapshot.aq1
                                response.CumQty.values += snapshot.aq1
                                response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                                response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                            responses.append(response)
                        else:
                            # Update the queue position
                            for index in range(1, 6):
                                px = eval('snapshot.order_book.b%d' % index)
                                qty = eval('snapshot.order_book.bq%d' % index)
                                if px == last_order_update.TriggeringInstruction.TriggerPrice.value:
                                    if qty < last_order_update.TriggeringInstruction.TriggerNewQty.value:
                                        # Volume reduced => Queuing position is fronter
                                        last_order_update.TriggeringInstruction.TriggerNewQty.value = qty
                                elif px < last_order_update.TriggeringInstruction.TriggerPrice.value and \
                                    px > 0.0:
                                    # No one is ahead of you now
                                    last_order_update.TriggeringInstruction.TriggerNewQty.value = 0
                    else:
                        if last_order_update.Price.value <- snapshot.b1 and \
                            last_order_update.Price > 0.0:
                            # Execution if the opposite best price equals or exceeds the price
                            response = deepcopy(last_order_update)
                            # Last price
                            response.LastPx.value = snapshot.b1
                            # Last quantity
                            response.LastQty.value = snapshot.bq1
                            # Leaves quantity and status
                            if snapshot.aq1 >= response.LeavesQty.value:
                                response.LeavesQty.value = 0
                                response.CumQty.values = response.OrderQtyData.OrderQty.value
                                response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                                response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                            else:
                                response.LeavesQty.value -= snapshot.bq1
                                response.CumQty.values += snapshot.bq1
                                response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                                response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                            responses.append(response)
                pass
            else:
                continue

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
        response.TriggeringInstruction.TriggerPrice.value = req.TriggeringInstruction.TriggerPrice.value
        response.TriggeringInstruction.TriggerNewQty.value = req.TriggeringInstruction.TriggerNewQty.value
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
        response.TriggeringInstruction.TriggerPrice.value = open_position[-1].TriggeringInstruction.TriggerPrice.value
        response.TriggeringInstruction.TriggerNewQty.value = open_position[-1].TriggeringInstruction.TriggerNewQty.value
        response.LeavesQty.value = 0
        response.LastQty.value = open_position[-1].LastQty.value
        response.CumQty.value = open_position[-1].CumQty.value
        response.LastPx.value = open_position[-1].LastPx.value
        return response



