#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.file_market_data_feed import FileMarketDataFeed
from bitz.exch_backtesting import ExchBacktesting
from bitz.logger import ConsoleLogger
from bitz.market_data import Snapshot, L2Depth, Trade
from datetime import datetime
import unittest


class TExchBacktesting(unittest.TestCase):
    def __create_new_single_order_best_bid(self, snapshot, side=Fix.Tags.Side.Values.BUY):
        """
        Create a NewSingleOrder
        :param snapshot: Instrument snapshot
        :return:
        """
        new_order_single = Fix.Messages.NewOrderSingle()
        new_order_single.Instrument.Symbol.value = snapshot.instmt
        new_order_single.Instrument.SecurityExchange.value = snapshot.exchange
        if side == Fix.Tags.Side.Values.BUY:
            new_order_single.Price.value = snapshot.order_book.b1
            new_order_single.Side.value = Fix.Tags.Side.Values.BUY
            new_order_single.TriggeringInstruction.TriggerPrice.value = snapshot.order_book.b1
            new_order_single.TriggeringInstruction.TriggerNewQty.value = snapshot.order_book.bq1
            new_order_single.ClOrdID.value = 'NewSingleBestBid%.6f' % snapshot.order_book.b1
        else:
            new_order_single.Price.value = snapshot.order_book.a1
            new_order_single.Side.value = Fix.Tags.Side.Values.SELL
            new_order_single.TriggeringInstruction.TriggerPrice.value = snapshot.order_book.a1
            new_order_single.TriggeringInstruction.TriggerNewQty.value = snapshot.order_book.aq1
            new_order_single.ClOrdID.value = 'NewSingleBestBid%.6f' % snapshot.order_book.a1

        new_order_single.OrderQtyData.OrderQty.value = 1
        new_order_single.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        new_order_single.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY
        return new_order_single

    def test_request_new_ack(self):
        # Initialize a file market data feed
        test_files = ['bitz\\test\\exch_quoine_btcusd_snapshot_20170407.csv']
        market_data_feed = FileMarketDataFeed(ConsoleLogger.static_logger)
        market_data_feed.connect(files=test_files)
        market_data_feed.get_snapshot(timeout=100)

        # Initialize the exchange quoine
        exch_snapshot = market_data_feed.snapshots[('quoine', 'btcusd')]
        exch = ExchBacktesting('quoine', market_data_feed, exch_snapshot)

        # Initialize the NewOrderSingle
        new_order_single = self.__create_new_single_order_best_bid(exch_snapshot)

        # Send the request
        responses, error = exch.request(new_order_single)
        response = responses[0]
        self.assertEqual(error, '')
        self.assertEqual(1, len(responses))
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

        order_cancel_request = Fix.Messages.OrderCancelRequest()
        order_cancel_request.Instrument.Symbol.value = response.Instrument.Symbol.value
        order_cancel_request.Instrument.SecurityExchange.value = response.Instrument.SecurityExchange.value
        new_order_single.ClOrdID.value = 'TestRequestNewAck2'
        order_cancel_request.OrderID.value = response.OrderID.value
        order_cancel_request.Side.value = response.Side.value

        # Send the request
        responses, error = exch.request(order_cancel_request)
        response = responses[0]
        self.assertEqual(error, '')
        self.assertEqual(1, len(responses))
        self.assertEqual(order_cancel_request.Instrument.SecurityExchange.value, response.Instrument.SecurityExchange.value)
        self.assertEqual(order_cancel_request.Instrument.Symbol.value, response.Instrument.Symbol.value)
        self.assertEqual(new_order_single.Price.value, response.Price.value)
        self.assertEqual(new_order_single.OrdType.value, response.OrdType.value)
        self.assertEqual(new_order_single.TimeInForce.value, response.TimeInForce.value)
        self.assertEqual(new_order_single.OrderQtyData.OrderQty.value, response.OrderQtyData.OrderQty.value)
        self.assertEqual(order_cancel_request.Side.value, response.Side.value)
        self.assertEqual(order_cancel_request.ClOrdID.value, response.ClOrdID.value)
        self.assertEqual(order_cancel_request.OrderID.value, response.OrderID.value)
        self.assertEqual(0, response.LeavesQty.value)
        self.assertEqual(0, response.LastQty.value)
        self.assertEqual(0, response.CumQty.value)
        self.assertEqual(0, response.LastPx.value)

if __name__ == '__main__':
    unittest.main()
