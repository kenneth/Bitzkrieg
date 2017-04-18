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
            update_fixtime(fix_response, Fix.Tags.TransactTime.Tag, self.__market_data_feed.now())
            # Ready to send
            fix_responses.append(fix_response)
            self.__open_positions[fix_response.OrderID.value] = [fix_response]

        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            if req.OrderID.value not in self.__open_positions.keys():
                # Reject with order not found
                raise NotImplementedError("Cancel rejection")
            elif self.__open_positions[req.OrderID.value][-1].LeavesQty.value == 0:
                # Reject completed order
                raise NotImplementedError("Cancel rejection")
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
            raise NotImplementedError("ORDERMASSSTATUSREQUEST")
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
        responses = []
        exchange = snapshot.exchange
        instmt = snapshot.instmt

        # For each open position, update the order status if necessary
        for order_id, order_updates in self.__open_positions.items():
            last_order_update = order_updates[-1]
            if last_order_update.Instrument.SecurityExchange.value == exchange and \
               last_order_update.Instrument.Symbol.value == instmt:
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

    def __prepare_position_report(self, req):
        fix_message = Fix.Messages.PositionReport()
        fix_message.Instrument.SecurityExchange.value = req.Instrument.SecurityExchange.value
        fix_message.ClearingBusinessDate.value = self.__market_data_feed.now().strftime("%Y%m%d")
        
        for currency, total_balance, available_balance in \
            [('USD', 1000, 1000),\
             ('HKD', 10000, 10000), \
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
                    response.LastQty.value = response.LeavesQty.value 
                    response.LeavesQty.value = 0
                    response.CumQty.value = response.OrderQtyData.OrderQty.value
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                else:
                    response.LastQty.value = snapshot.order_book.aq1
                    response.LeavesQty.value -= snapshot.order_book.aq1
                    response.CumQty.value += snapshot.order_book.aq1
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
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
                    response.LastQty.value = response.LeavesQty.value 
                    response.LeavesQty.value = 0
                    response.CumQty.value = response.OrderQtyData.OrderQty.value
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                else:
                    response.LastQty.value = snapshot.order_book.bq1                    
                    response.LeavesQty.value -= snapshot.order_book.bq1
                    response.CumQty.value += snapshot.order_book.bq1
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
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
        if snapshot.last_trade.trade_price == last_order_update.Price.value:
            if last_order_update.TriggeringInstruction.TriggerNewQty.value - snapshot.last_trade.trade_volume < 0:
                # The order got filled
                response = deepcopy(last_order_update)
                trade_volume = snapshot.last_trade.trade_volume - last_order_update.TriggeringInstruction.TriggerNewQty.value
                # Last price
                response.LastPx.value = snapshot.last_trade.trade_price
                # Leaves quantity and status
                if trade_volume >= response.LeavesQty.value:
                    response.LastQty.value = response.LeavesQty.value
                    response.LeavesQty.value = 0
                    response.CumQty.value = response.OrderQtyData.OrderQty.value
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE
                else:
                    response.LastQty.value = trade_volume
                    response.LeavesQty.value -= trade_volume
                    response.CumQty.values += trade_volume
                    response.OrdStatus.value = Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED
                    response.ExecType.value = Fix.Tags.ExecType.Values.TRADE   
                    
                response.TriggeringInstruction.TriggerNewQty.value = 0
                return response
            else:
                # The order is not filled but the queue position is better now
                last_order_update.TriggeringInstruction.TriggerNewQty -= snapshot.last_trade.trade_volume
        
        return None