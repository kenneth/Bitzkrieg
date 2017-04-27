#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.file_market_data_feed import FileMarketDataFeed
from bitz.exch_backtesting import ExchBacktesting
from bitz.logger import ConsoleLogger
from bitz.market_data import Snapshot, L2Depth, Trade
from datetime import datetime
from uuid import uuid4 as uuid
import unittest
import os

class TExchBacktesting(unittest.TestCase):
    def __initialise_exchange(self):
        """
        Initialize the exchange from file handler
        """
        # Initialize a file market data feed
        test_files = [os.path.join('bitz', 'test', 'exch_quoine_btcusd_snapshot_20170407.csv')]
        market_data_feed = FileMarketDataFeed(ConsoleLogger.static_logger)
        market_data_feed.connect(files=test_files)
        market_data_feed.get_snapshot(timeout=100)

        # Initialize the exchange quoine
        exch_snapshot = market_data_feed.snapshots[('quoine', 'btcusd')]
        exch = ExchBacktesting('quoine', market_data_feed, exch_snapshot)
        
        return market_data_feed, exch_snapshot, exch
    
    def __create_new_single_order(self, snapshot, price, qty, side=Fix.Tags.Side.Values.BUY):
        """
        Create a NewSingleOrder
        :param snapshot: Instrument snapshot
        :param price: Price
        :param qty: Quantity
        :param triggerqty: Trigger Qty
        :param side: Side
        :return: NewSingleOrder
        """
        new_order_single = Fix.Messages.NewOrderSingle()
        new_order_single.Instrument.Symbol.value = snapshot.instmt
        new_order_single.Instrument.SecurityExchange.value = snapshot.exchange
        new_order_single.Price.value = price
        new_order_single.TriggeringInstruction.TriggerPrice.value = price
        new_order_single.Side.value = side
        new_order_single.ClOrdID.value = uuid()
        new_order_single.OrderQtyData.OrderQty.value = qty
        new_order_single.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        new_order_single.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY
        
        # Set triggering quantity. If the price is not with the first 5 price range,
        # set it as 0 for triggering quantity.
        new_order_single.TriggeringInstruction.TriggerPrice.value = price
        new_order_single.TriggeringInstruction.TriggerNewQty.value = 0
        if side == Fix.Tags.Side.Values.BUY:
            for tpx, tqty in [(snapshot.order_book.b1, snapshot.order_book.bq1), \
                            (snapshot.order_book.b2, snapshot.order_book.bq2), \
                            (snapshot.order_book.b3, snapshot.order_book.bq3), \
                            (snapshot.order_book.b4, snapshot.order_book.bq4), \
                            (snapshot.order_book.b5, snapshot.order_book.bq5)]:      
                if tpx == new_order_single.TriggeringInstruction.TriggerPrice.value:
                    new_order_single.TriggeringInstruction.TriggerNewQty.value = tqty
                    break
        else:
            for tpx, tqty in [(snapshot.order_book.a1, snapshot.order_book.aq1), \
                            (snapshot.order_book.a2, snapshot.order_book.aq2), \
                            (snapshot.order_book.a3, snapshot.order_book.aq3), \
                            (snapshot.order_book.a4, snapshot.order_book.aq4), \
                            (snapshot.order_book.a5, snapshot.order_book.aq5)]:      
                if tpx == new_order_single.TriggeringInstruction.TriggerPrice.value:
                    new_order_single.TriggeringInstruction.TriggerNewQty.value = tqty
                    break            
                
        return new_order_single
        
    def __create_new_single_order_at_best(self, snapshot, side=Fix.Tags.Side.Values.BUY):
        """
        Create a NewSingleOrder at the best price
        :param snapshot: Instrument snapshot
        :return: NewSingleOrder
        """
        if side == Fix.Tags.Side.Values.BUY:
            return self.__create_new_single_order(snapshot, snapshot.order_book.b1, 1, side)
        else:
            return self.__create_new_single_order(snapshot, snapshot.order_book.a1, 1, side)
        
    def __assert_execution_report_exectype_new(self, new_order_single, response):
        """
        Assert execution report for ExecType=NEW
        :param new_order_single: NewOrderSingle
        :param response: FIX update
        """
        self.assertEqual(Fix.Tags.OrdStatus.Values.NEW, response.OrdStatus.value)
        self.assertEqual(Fix.Tags.ExecType.Values.NEW, response.ExecType.value)
        self.assertEqual(new_order_single.Instrument.SecurityExchange.value, response.Instrument.SecurityExchange.value)
        self.assertEqual(new_order_single.Instrument.Symbol.value, response.Instrument.Symbol.value)
        self.assertEqual(new_order_single.Price.value, response.Price.value)
        self.assertEqual(new_order_single.OrdType.value, response.OrdType.value)
        self.assertEqual(new_order_single.TimeInForce.value, response.TimeInForce.value)
        self.assertEqual(new_order_single.OrderQtyData.OrderQty.value, response.OrderQtyData.OrderQty.value)
        self.assertEqual(new_order_single.Side.value, response.Side.value)
        self.assertEqual(new_order_single.ClOrdID.value, response.ClOrdID.value)
        self.assertEqual(response.OrderQtyData.OrderQty.value, response.LeavesQty.value)
        self.assertEqual(0, response.LastQty.value)
        self.assertEqual(0, response.CumQty.value)
        self.assertEqual(0, response.LastPx.value)        
        self.assertEqual(new_order_single.TriggeringInstruction.TriggerPrice.value, response.TriggeringInstruction.TriggerPrice.value)
        self.assertEqual(new_order_single.TriggeringInstruction.TriggerNewQty.value, response.TriggeringInstruction.TriggerNewQty.value)   
        
    def __assert_execution_report_exectype_canceled(self, order_cancel_request, pre_cancel_response, response):
        """
        Assert execution report with ExecType=CANCELED
        :param order_cancel_request: OrderCancelRequest
        :param pre_cancel_response: The last execution report before cancellation
        :param response: The execution report of cancellation
        """
        self.assertEqual(Fix.Tags.OrdStatus.Values.CANCELED, response.OrdStatus.value)
        self.assertEqual(Fix.Tags.ExecType.Values.CANCELED, response.ExecType.value)        
        self.assertEqual(order_cancel_request.Instrument.SecurityExchange.value, response.Instrument.SecurityExchange.value)
        self.assertEqual(order_cancel_request.Instrument.Symbol.value, response.Instrument.Symbol.value)
        self.assertEqual(order_cancel_request.ClOrdID.value, response.ClOrdID.value)
        self.assertEqual(pre_cancel_response.Price.value, response.Price.value)
        self.assertEqual(pre_cancel_response.OrdType.value, response.OrdType.value)
        self.assertEqual(pre_cancel_response.TimeInForce.value, response.TimeInForce.value)
        self.assertEqual(pre_cancel_response.OrderQtyData.OrderQty.value, response.OrderQtyData.OrderQty.value)
        self.assertEqual(pre_cancel_response.Side.value, response.Side.value)
        self.assertEqual(pre_cancel_response.OrderID.value, response.OrderID.value)
        self.assertEqual(pre_cancel_response.LastQty.value, response.LastQty.value)
        self.assertEqual(pre_cancel_response.CumQty.value, response.CumQty.value)
        self.assertEqual(pre_cancel_response.LastPx.value, response.LastPx.value)
        self.assertEqual(0, response.LeavesQty.value)
        
    def __assert_execution_report_exectype_trade(self, pre_execution, response, last_qty, leaves_qty):
        """
        Assert execution report with ExecType=CANCELED
        :param pre_execution: The last execution report before cancellation
        :param response: The execution report of cancellation
        :param leaves_qty: The quantity expected to be left in the market
        """        
        if leaves_qty == 0:
            self.assertEqual(Fix.Tags.OrdStatus.Values.FILLED, response.OrdStatus.value)
        else:
            self.assertEqual(Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED, response.OrdStatus.value)
            
        self.assertEqual(Fix.Tags.ExecType.Values.TRADE, response.ExecType.value)                
        self.assertEqual(pre_execution.Instrument.SecurityExchange.value, response.Instrument.SecurityExchange.value)
        self.assertEqual(pre_execution.Instrument.Symbol.value, response.Instrument.Symbol.value)
        self.assertEqual(pre_execution.ClOrdID.value, response.ClOrdID.value)      
        self.assertEqual(pre_execution.Price.value, response.Price.value)
        self.assertEqual(pre_execution.OrdType.value, response.OrdType.value)
        self.assertEqual(pre_execution.TimeInForce.value, response.TimeInForce.value)
        self.assertEqual(pre_execution.OrderQtyData.OrderQty.value, response.OrderQtyData.OrderQty.value)
        self.assertEqual(pre_execution.Side.value, response.Side.value)
        self.assertEqual(pre_execution.OrderID.value, response.OrderID.value)
        self.assertEqual(response.LastQty.value, last_qty)
        self.assertEqual(response.CumQty.value, response.OrderQtyData.OrderQty.value - leaves_qty)
        self.assertEqual(response.LastPx.value, response.Price.value)
        self.assertEqual(response.LeavesQty.value, leaves_qty)        

    def __assert_execution_report_exectype_cancelReject(self, order_cancel_request, response):
        """
        Assert OrderCancelReject Msg
        :param order_cancel_request: OrderCancelRequest
        :param response: The order cancel reject response
        :return: 
        """
        self.assertEqual(Fix.Tags.OrdStatus.Values.REJECTED, response.OrdStatus.value)
        self.assertEqual(Fix.Tags.CxlRejResponseTo.Values.ORDER_CANCEL_REQUEST, response.CxlRejResponseTo.value)
        self.assertEqual(order_cancel_request.OrderID.value, response.OrderID.value)
        self.assertEqual(order_cancel_request.ClOrdID.value, response.ClOrdID.value)

    def test_request_new_ack(self):
        """
        Test the order is placed and acknowledged. Then the order is cancelled without any fills
        """
        # Initialization
        market_data_feed, exch_snapshot, exch = self.__initialise_exchange()

        # Initialize the NewOrderSingle
        new_order_single = self.__create_new_single_order_at_best(exch_snapshot)

        # Send the request
        ack_responses, error = exch.request(new_order_single)
        self.assertEqual(error, '')
        self.assertEqual(1, len(ack_responses))
        ack_response = ack_responses[0]
        self.__assert_execution_report_exectype_new(new_order_single, ack_response)

        for i in range(0, 5):
            snapshot = market_data_feed.get_snapshot(timeout=0)
            exch.snapshot_updated(snapshot)
            last_status = exch.get_latest_status(ack_response.OrderID.value)
            self.assertEqual(last_status.TriggeringInstruction.TriggerPrice.value, new_order_single.TriggeringInstruction.TriggerPrice.value)
            self.assertEqual(last_status.TriggeringInstruction.TriggerNewQty.value, exch_snapshot.order_book.bq1)

        # The triggering volume reduced to 0.99 before cancellation
        self.assertEqual(last_status.TriggeringInstruction.TriggerNewQty.value, 0.99)

        order_cancel_request = Fix.Messages.OrderCancelRequest()
        order_cancel_request.Instrument.Symbol.value = new_order_single.Instrument.Symbol.value
        order_cancel_request.Instrument.SecurityExchange.value = new_order_single.Instrument.SecurityExchange.value
        order_cancel_request.ClOrdID.value = uuid()
        order_cancel_request.OrderID.value = ack_response.OrderID.value
        order_cancel_request.Side.value = new_order_single.Side.value

        # Send the request
        cancel_responses, error = exch.request(order_cancel_request)
        self.assertEqual(1, len(cancel_responses))
        self.assertEqual(error, '')
        cancel_response = cancel_responses[0]
        self.__assert_execution_report_exectype_canceled(order_cancel_request, ack_response, cancel_response)

    def test_fully_filled_by_trade_update(self):
        """
        Test the order is placed and then filled due to trade update.
        """
        # Initialization
        market_data_feed, exch_snapshot, exch = self.__initialise_exchange()

        # Initialize the NewOrderSingle
        new_order_single = self.__create_new_single_order_at_best(exch_snapshot)

        # Send the request
        ack_responses, error = exch.request(new_order_single)
        self.assertEqual(error, '')
        self.assertEqual(1, len(ack_responses))
        ack_response = ack_responses[0]
        self.__assert_execution_report_exectype_new(new_order_single, ack_response)        

        for i in range(0, 5):
            snapshot = market_data_feed.get_snapshot(timeout=0)
            exch.snapshot_updated(snapshot)
        
        # Filled at the sixth update
        snapshot = market_data_feed.get_snapshot(timeout=0)
        exch.snapshot_updated(snapshot)
        last_status = exch.get_latest_status(ack_response.OrderID.value)
        self.__assert_execution_report_exectype_trade(ack_response, last_status, ack_response.OrderQtyData.OrderQty.value, 0)

    def test_fully_filled_by_price_update(self):
        """
        Test the order is placed and then filled due to price update.
        """
        # Initialization
        market_data_feed, exch_snapshot, exch = self.__initialise_exchange()

        # Initialize the NewOrderSingle
        new_order_single = self.__create_new_single_order(exch_snapshot, exch_snapshot.order_book.a1 - 0.1, 1)

        # Send the request
        ack_responses, error = exch.request(new_order_single)
        self.assertEqual(error, '')
        self.assertEqual(1, len(ack_responses))
        ack_response = ack_responses[0]
        self.__assert_execution_report_exectype_new(new_order_single, ack_response)        

        for i in range(0, 4):
            snapshot = market_data_feed.get_snapshot(timeout=0)
            exch.snapshot_updated(snapshot)
        
        # Filled at the fifth update
        snapshot = market_data_feed.get_snapshot(timeout=0)
        exch.snapshot_updated(snapshot)
        last_status = exch.get_latest_status(ack_response.OrderID.value)
        self.__assert_execution_report_exectype_trade(ack_response, last_status, ack_response.OrderQtyData.OrderQty.value, 0)   

    def test_triggering_quantity_remain_same(self):
        """
        Test the order is placed at the a5 and the queue position remains when the price never appears again in the order book.
        """
        # Initialization
        market_data_feed, exch_snapshot, exch = self.__initialise_exchange()

        # Initialize the NewOrderSingle
        new_order_single = self.__create_new_single_order(exch_snapshot, exch_snapshot.order_book.a5, 1, Fix.Tags.Side.Values.SELL)

        # Send the request
        ack_responses, error = exch.request(new_order_single)
        self.assertEqual(error, '')
        self.assertEqual(1, len(ack_responses))
        ack_response = ack_responses[0]
        self.__assert_execution_report_exectype_new(new_order_single, ack_response)    
        self.assertEqual(ack_response.TriggeringInstruction.TriggerPrice.value, exch_snapshot.order_book.a5)
        self.assertEqual(ack_response.TriggeringInstruction.TriggerNewQty.value, exch_snapshot.order_book.aq5)

        # Never appears back to the order book but the queue position remains the same
        for i in range(0, 100):
            snapshot = market_data_feed.get_snapshot(timeout=0)
            exch.snapshot_updated(snapshot)
            last_status = exch.get_latest_status(ack_response.OrderID.value)
            self.assertEqual(ack_response.TriggeringInstruction.TriggerPrice.value, last_status.TriggeringInstruction.TriggerPrice.value)
            self.assertEqual(ack_response.TriggeringInstruction.TriggerNewQty.value, last_status.TriggeringInstruction.TriggerNewQty.value)

    def test_triggering_quantity_reduce(self):
        """
        Test the order is placed at the a5 and the queue position remains when the price never appears again in the order book.
        """
        # Initialization
        market_data_feed, exch_snapshot, exch = self.__initialise_exchange()

        # Initialize the NewOrderSingle
        new_order_single = self.__create_new_single_order(exch_snapshot, exch_snapshot.order_book.b4, 1)

        # Send the request
        ack_responses, error = exch.request(new_order_single)
        self.assertEqual(error, '')
        self.assertEqual(1, len(ack_responses))
        ack_response = ack_responses[0]
        self.__assert_execution_report_exectype_new(new_order_single, ack_response)    
        self.assertEqual(ack_response.TriggeringInstruction.TriggerPrice.value, exch_snapshot.order_book.b4)
        self.assertEqual(ack_response.TriggeringInstruction.TriggerNewQty.value, exch_snapshot.order_book.bq4)

        # Remains the same in the first 9 updates, but reduced in the 10th updates
        for i in range(0, 10):
            snapshot = market_data_feed.get_snapshot(timeout=0)
            exch.snapshot_updated(snapshot)
            last_status = exch.get_latest_status(ack_response.OrderID.value)
            if i < 9:
                self.assertEqual(ack_response.TriggeringInstruction.TriggerPrice.value, last_status.TriggeringInstruction.TriggerPrice.value)
                self.assertEqual(ack_response.TriggeringInstruction.TriggerNewQty.value, last_status.TriggeringInstruction.TriggerNewQty.value)
            else:
                self.assertEqual(ack_response.TriggeringInstruction.TriggerPrice.value, last_status.TriggeringInstruction.TriggerPrice.value)
                self.assertEqual(ack_response.TriggeringInstruction.TriggerNewQty.value, exch_snapshot.order_book.bq1)                
    
    def test_request_positions(self):
        """
        Test request positions
        """
        # Initialization
        market_data_feed, exch_snapshot, exch = self.__initialise_exchange()
        
        # Request positions
        req = Fix.Messages.RequestForPositions()
        req.PosReqID.value = "Request positions"
        req.Instrument.SecurityExchange.value = 'quoine'
        responses, err_msg = exch.request(req)    
        self.assertEqual(1, len(responses))
        
        positions = responses[0]
        self.assertEqual(6, len(positions.PositionAmountData.groups))
        self.assertEqual(positions.PositionAmountData.groups[0].PositionCurrency.value, "USD")
        self.assertEqual(positions.PositionAmountData.groups[0].PosAmt.value, 2000)
        self.assertEqual(positions.PositionAmountData.groups[0].PosAmtType.value, Fix.Tags.PosAmtType.Values.CASH_AMOUNT)
        self.assertEqual(positions.PositionAmountData.groups[1].PositionCurrency.value, "USD")
        self.assertEqual(positions.PositionAmountData.groups[1].PosAmt.value, 2000)
        self.assertEqual(positions.PositionAmountData.groups[1].PosAmtType.value, Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT)        
        self.assertEqual(positions.PositionAmountData.groups[2].PositionCurrency.value, "HKD")
        self.assertEqual(positions.PositionAmountData.groups[2].PosAmt.value, 100000)
        self.assertEqual(positions.PositionAmountData.groups[2].PosAmtType.value, Fix.Tags.PosAmtType.Values.CASH_AMOUNT)
        self.assertEqual(positions.PositionAmountData.groups[3].PositionCurrency.value, "HKD")
        self.assertEqual(positions.PositionAmountData.groups[3].PosAmt.value, 100000)
        self.assertEqual(positions.PositionAmountData.groups[3].PosAmtType.value, Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT)   
        self.assertEqual(positions.PositionAmountData.groups[4].PositionCurrency.value, "BTC")
        self.assertEqual(positions.PositionAmountData.groups[4].PosAmt.value, 10)
        self.assertEqual(positions.PositionAmountData.groups[4].PosAmtType.value, Fix.Tags.PosAmtType.Values.CASH_AMOUNT)
        self.assertEqual(positions.PositionAmountData.groups[5].PositionCurrency.value, "BTC")
        self.assertEqual(positions.PositionAmountData.groups[5].PosAmt.value, 10)
        self.assertEqual(positions.PositionAmountData.groups[5].PosAmtType.value, Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT)

    def test_cancel_rejected_after_fully_fill(self):
        """
        Test  order cancel after fully fill is rejected as too late
        """
        # Initialization
        market_data_feed, exch_snapshot, exch = self.__initialise_exchange()

        # Initialize the NewOrderSingle
        new_order_single = self.__create_new_single_order_at_best(exch_snapshot)

        # Send the request
        ack_responses, error = exch.request(new_order_single)
        self.assertEqual(error, '')
        self.assertEqual(1, len(ack_responses))
        ack_response = ack_responses[0]
        self.__assert_execution_report_exectype_new(new_order_single, ack_response)

        for i in range(0, 5):
            snapshot = market_data_feed.get_snapshot(timeout=0)
            exch.snapshot_updated(snapshot)

        # Filled at the sixth update
        snapshot = market_data_feed.get_snapshot(timeout=0)
        exch.snapshot_updated(snapshot)
        last_status = exch.get_latest_status(ack_response.OrderID.value)
        self.__assert_execution_report_exectype_trade(ack_response, last_status,
                                                      ack_response.OrderQtyData.OrderQty.value, 0)

        order_cancel_request = Fix.Messages.OrderCancelRequest()
        order_cancel_request.Instrument.Symbol.value = new_order_single.Instrument.Symbol.value
        order_cancel_request.Instrument.SecurityExchange.value = new_order_single.Instrument.SecurityExchange.value
        order_cancel_request.ClOrdID.value = uuid()
        order_cancel_request.OrderID.value = ack_response.OrderID.value
        order_cancel_request.Side.value = new_order_single.Side.value

        # Send (late) cancel request, should be rejected
        cancel_responses, error = exch.request(order_cancel_request)
        self.assertEqual(1, len(cancel_responses))
        self.assertEqual(error, '')
        cancel_response = cancel_responses[0]
        self.__assert_execution_report_exectype_cancelReject(order_cancel_request, cancel_response)

if __name__ == '__main__':
    unittest.main()
