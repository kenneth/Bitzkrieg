#!/usr/bin/python3
from bitz.exchange import Exchange
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.util import update_fixtime
from copy import deepcopy
from uuid import uuid4 as uuid

class ExchBacktesting(Exchange):
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
        Exchange.__init__(self)
        self.__name = name
        self.__market_data_feed = market_data_feed
        self.__network_latency = network_latency
        self.__exch_order_id = 0
        self.__open_positions = {}
        self.__price_gap_detection = 100

    def get_name(self):
        """
        Get name
        """
        return self.__name

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
            snapshot = self.__market_data_feed.get_exchange_snapshot(exchange, instmt)
            if snapshot is None:
                # Reject the order with invalid instrument
                raise NotImplementedError("Ack rejection")
            else:
                fix_response = self.__prepare_exectype_new(req)
            # else:
            #     # Ignore the case of rejection first
            #     fix_response.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
            #     fix_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
            #     fix_response.OrdRejReason.value = Fix.Tags.OrdRejReason.Values.OTHER
            #     fix_response.Text.value = "Rejected by the exchange."

            # Add TransactTime
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag, now_time=self.__market_data_feed.now_string())
            # Ready to send
            fix_responses.append(fix_response)
            self.__open_positions[fix_response.OrderID.value] = [fix_response]

        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            if req.OrderID.value not in self.__open_positions.keys():
                # Reject with order not found
                raise NotImplementedError("Cancel rejection")
            elif self.__open_positions[req.OrderID.value][-1].LeavesQty.value == 0:
                # Reject completed order
                fix_response = self.__prepare_exectype_cancelReject(req)
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
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag, now_time=self.__market_data_feed.now_string())
            # Ready to send
            fix_responses.append(fix_response)
            # Update the open positions
            self.__open_positions[req.OrderID.value].append(fix_response)

        elif msgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            raise NotImplementedError("ORDERMASSSTATUSREQUEST")
        elif msgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST:
            order_id = req.OrderID.value
            if order_id in self.__open_positions.keys():
                last_order_update = deepcopy(self.__open_positions[order_id][-1])
                last_order_update.ExecType.value = Fix.Tags.ExecType.Values.ORDER_STATUS
                last_order_update.ExecID.value = self.__market_data_feed.now_string() + str(uuid())
                fix_responses.append(last_order_update)
            else:
                raise NotImplementedError("Reject not found order id" % order_id)
        elif msgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            fix_responses.append(self.__prepare_position_report(req))
        else:
            raise NotImplementedError("MsgType %s request has not been implemented." % msgType)

        return fix_responses, err_msg

    def snapshot_updated(self, snapshot):
        """
        Snapshot updated
        :param snapshot: The instrument snapshot
        :return FIX message responses if provided.
        """
        exchange = snapshot.exchange
        instmt = snapshot.instmt

        # For each open position, update the order status if necessary
        for order_id, order_updates in self.__open_positions.items():
            last_order_update = order_updates[-1]
            if last_order_update.Instrument.SecurityExchange.value.upper() == exchange and \
               last_order_update.Instrument.Symbol.value.upper() == instmt and \
               last_order_update.LeavesQty.value > 0:
                response = None
                if snapshot.update_type == snapshot.UpdateType.ORDER_BOOK:
                    response = self.__update_last_execution_report_price_update(snapshot, last_order_update)
                elif snapshot.update_type == snapshot.UpdateType.TRADES:
                    response = self.__update_last_execution_report_trade_update(snapshot, last_order_update)
                else:
                    pass
                
                # Add the execution at the back if provided
                if response is not None:
                    order_updates.append(response)                
            else:
                continue
        
        return None

    def get_latest_status(self, order_id):
        """
        Get the latest status given an order id
        :param order_id: Order ID
        :return The last execution report
        """
        assert order_id in self.__open_positions.keys(), "Invalid order ID %s" % order_id
        return self.__open_positions[order_id][-1]

    def __get_next_exch_order_id(self):
        """
        Get the next exchange order id
        :return: Exchange order id, an integer
        """
        self.__exch_order_id += 1
        return self.__exch_order_id

    def __update_volume_fill_information(self, response: Fix.Messages.ExecutionReport, trade_px, trade_vol):
        """
        Update volume fill information, e.g. CumQty, AvgQty, LastPx, LastQty and LeavesQty
        :param response: Execution report
        :param trade_px: Trade price
        :param trade_vol: Trade volume
        """
        prev_cumqty = response.CumQty.value
        prev_avgpx = response.AvgPx.value
        prev_leavesqty = response.LeavesQty.value

        response.LastPx.value = trade_px
        response.LastQty.value = trade_vol

        if prev_cumqty is None:
            response.AvgPx.value = trade_px
            response.CumQty.value = trade_vol
        else:
            response.AvgPx.value = (prev_cumqty * prev_avgpx + trade_vol * trade_px) / (prev_cumqty + trade_vol)
            response.CumQty.value = prev_cumqty + trade_vol

        if prev_leavesqty is None or prev_leavesqty > 0.0:
            response.LeavesQty.value = response.OrderQtyData.OrderQty.value - response.CumQty.value

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
        self.__update_volume_fill_information(response, 0, 0)
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
        response.AvgPx.value = open_position[-1].AvgPx.value
        return response

    def __prepare_exectype_cancelReject(self, req):
        """
        Prepare order cancel reject
        :param req: Order request
        :return: Order cancel reject
        """
        assert req.OrderID.value in self.__open_positions.keys()
        open_position = self.__open_positions[req.OrderID.value]
        response = Fix.Messages.OrderCancelReject()
        response.ClOrdID.value = req.ClOrdID.value
        response.OrderID.value = req.OrderID.value
        response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
        response.CxlRejResponseTo.value = Fix.Tags.CxlRejResponseTo.Values.ORDER_CANCEL_REQUEST
        response.Text.value = 'Cancel rejected by exchange'
        response.CxlRejReason.value = Fix.Tags.CxlRejReason.Values.OTHER
        return response

    def __prepare_position_report(self, req):
        fix_message = Fix.Messages.PositionReport()
        fix_message.PosReqID.value = req.PosReqID.value
        fix_message.Instrument.SecurityExchange.value = req.Instrument.SecurityExchange.value
        fix_message.ClearingBusinessDate.value = self.__market_data_feed.now_string("%Y%m%d")
        fix_message.PosMaintRptID.value = self.__market_data_feed.now_string() + str(uuid())
        
        for currency, total_balance, available_balance in \
            [('USD', 2000, 2000),
             ('HKD', 100000, 100000),
             ('BTC', 10, 10)]:
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

    def __update_last_execution_report_price_update(self, snapshot, last_order_update):
        """
        Update last execution report based on price update.
        
        :param snapshot: Snapshot
        :param last_order_update: The last execution report
        :return Fill execution reports if there is any fills. None if the execution
                report is updated only. (Only on TriggeringInstruction)
        """
        if last_order_update.Side.value == Fix.Tags.Side.Values.BUY:
            # BUY
            if last_order_update.Price.value >= snapshot.order_book.a1 and \
                snapshot.order_book.a1 > 0.0:
                # Execution if the opposite best price equals or exceeds the price
                response = deepcopy(last_order_update)
                # Last price
                response.LastPx.value = response.Price.value
                # Leaves quantity and status
                if snapshot.order_book.aq1 >= response.LeavesQty.value:
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                    self.__update_volume_fill_information(response, response.Price.value, response.LeavesQty.value)
                else:
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                    self.__update_volume_fill_information(response, response.Price.value, snapshot.order_book.aq1)
                return response
            else:
                # Update the queue position
                for px, qty in [(snapshot.order_book.b1, snapshot.order_book.bq1), \
                                (snapshot.order_book.b2, snapshot.order_book.bq2), \
                                (snapshot.order_book.b3, snapshot.order_book.bq3), \
                                (snapshot.order_book.b4, snapshot.order_book.bq4), \
                                (snapshot.order_book.b5, snapshot.order_book.bq5)]:
                    if px == last_order_update.TriggeringInstruction.TriggerPrice.value:
                        if qty < last_order_update.TriggeringInstruction.TriggerNewQty.value:
                            # Volume reduced => Queuing position is fronter
                            last_order_update.TriggeringInstruction.TriggerNewQty.value = qty
                        break
                    elif px < last_order_update.TriggeringInstruction.TriggerPrice.value and \
                        px > 0.0:
                        # No one is ahead of you now
                        last_order_update.TriggeringInstruction.TriggerNewQty.value = 0
                return None
        else:
            if last_order_update.Price.value <= snapshot.order_book.b1 and \
                last_order_update.Price > 0.0:
                # Execution if the opposite best price equals or exceeds the price
                response = deepcopy(last_order_update)
                # Last price
                response.LastPx.value = response.Price.value
                # Leaves quantity and status
                if snapshot.order_book.bq1 >= response.LeavesQty.value:
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                    self.__update_volume_fill_information(response, response.Price.value, response.LeavesQty.value)
                else:
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                    self.__update_volume_fill_information(response, response.Price.value, snapshot.order_book.bq1)
                return response
            else:
                # Update the queue position
                for px, qty in [(snapshot.order_book.a1, snapshot.order_book.aq1), \
                                (snapshot.order_book.a2, snapshot.order_book.aq2), \
                                (snapshot.order_book.a3, snapshot.order_book.aq3), \
                                (snapshot.order_book.a4, snapshot.order_book.aq4), \
                                (snapshot.order_book.a5, snapshot.order_book.aq5)]:
                    if px == last_order_update.TriggeringInstruction.TriggerPrice.value:
                        if qty < last_order_update.TriggeringInstruction.TriggerNewQty.value:
                            # Volume reduced => Queuing position is fronter
                            last_order_update.TriggeringInstruction.TriggerNewQty.value = qty
                        break
                    elif px > last_order_update.TriggeringInstruction.TriggerPrice.value and \
                        px > last_order_update.TriggeringInstruction.TriggerPrice.value:
                        # No one is ahead of you now
                        last_order_update.TriggeringInstruction.TriggerNewQty.value = 0
                return None                

    def __update_last_execution_report_trade_update(self, snapshot, last_order_update):
        """
        Update last execution report based on trade update.
        
        :param snapshot: Snapshot
        :param last_order_update: The last execution report
        :return Fill execution reports if there is any fills. None if the execution
                report is updated only. (Only on TriggeringInstruction)
        """
        if (last_order_update.Side.value == Fix.Tags.Side.Values.BUY and
                snapshot.last_trade.trade_price <= last_order_update.Price.value) or \
            (last_order_update.Side.value == Fix.Tags.Side.Values.SELL and
                snapshot.last_trade.trade_price >= last_order_update.Price.value):
            if last_order_update.TriggeringInstruction.TriggerNewQty.value - snapshot.last_trade.trade_volume < 0:
                # The order got filled
                response = deepcopy(last_order_update)
                trade_volume = snapshot.last_trade.trade_volume - last_order_update.TriggeringInstruction.TriggerNewQty.value
                # Last price
                response.LastPx.value = snapshot.last_trade.trade_price
                # Leaves quantity and status
                if trade_volume >= response.LeavesQty.value:
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                    self.__update_volume_fill_information(response, response.Price.value, response.LeavesQty.value)
                else:
                    response.LastQty.value = trade_volume
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                    self.__update_volume_fill_information(response, response.Price.value, trade_volume)

                response.TriggeringInstruction.TriggerNewQty.value = 0
                return response
            else:
                # The order is not filled but the queue position is better now
                last_order_update.TriggeringInstruction.TriggerNewQty -= snapshot.last_trade.trade_volume
        
        return None