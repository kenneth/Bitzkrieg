#!/bin/python
from bitz.file_market_data_feed import FileMarketDataFeed
from bitz.logger import ConsoleLogger
from bitz.market_data import Snapshot, L2Depth, Trade
from datetime import datetime
import unittest
import os


class TFileMarketDataFeed(unittest.TestCase):
    def test_connect_single_file(self):
        test_files = [os.path.join('bitz', 'test', 'exch_quoine_btcusd_snapshot_20170407.csv')]
        data_feed = FileMarketDataFeed(ConsoleLogger.static_logger)

        # Connect
        self.assertTrue(data_feed.connect(files=test_files))
        self.assertEqual(datetime(2017, 4, 7, 0, 0, 38, 301868), data_feed.now())

        # Get snapshot for a very short timeout period
        ret = data_feed.get_snapshot(timeout=1)
        self.assertIsInstance(ret, int)
        self.assertEqual(ret, 0)
        snapshot = data_feed.get_exchange_snapshot('quoine', 'btcusd')
        self.assertEqual(1190.7, snapshot.order_book.b1)
        self.assertEqual(1192.29, snapshot.order_book.a1)
        self.assertEqual(1.99, snapshot.order_book.bq1)
        self.assertEqual(0.01383556, snapshot.order_book.aq1)
        self.assertEqual(0, snapshot.last_trade.trade_price)
        self.assertEqual(0, snapshot.last_trade.trade_volume)

        self.assertEqual(datetime(2017, 4, 7, 0, 0, 38, 301869), data_feed.now())

        # Get snapshot with timeout = 30 mins
        ret = data_feed.get_snapshot(timeout=1000000 * 60 * 30)
        self.assertIsInstance(ret, Snapshot)
        self.assertEqual('QUOINE', ret.exchange)
        self.assertEqual('BTCUSD', ret.instmt)
        self.assertEqual(1190.7, ret.order_book.b1)
        self.assertEqual(1192.3, ret.order_book.a1)
        self.assertEqual(1.99, ret.order_book.bq1)
        self.assertEqual(6.64, ret.order_book.aq1)
        self.assertEqual(0, ret.last_trade.trade_price)
        self.assertEqual(0, ret.last_trade.trade_volume)
        self.assertEqual(datetime(2017, 4, 7, 0, 0, 48, 770277), data_feed.now())

        data_feed.disconnect()

    def test_connect_multiple_files(self):
        test_files = [os.path.join('bitz', 'test', 'exch_quoine_btcusd_snapshot_20170407.csv'),
                      os.path.join('bitz', 'test', 'exch_gatecoin_btchkd_snapshot_20170407.csv')]
        data_feed = FileMarketDataFeed(ConsoleLogger.static_logger)

        # Connect
        self.assertTrue(data_feed.connect(files=test_files))
        self.assertEqual(datetime(2017, 4, 7, 0, 0, 38, 301868), data_feed.now())

        # Get snapshot for a very short timeout period
        ret = data_feed.get_snapshot(timeout=1)
        self.assertIsInstance(ret, int)
        self.assertEqual(ret, 0)
        self.assertEqual(datetime(2017, 4, 7, 0, 0, 38, 301869), data_feed.now())

        # Get snapshot with timeout = 30 mins
        ret = data_feed.get_snapshot(timeout=1000000 * 60 * 30)
        self.assertIsInstance(ret, Snapshot)
        self.assertEqual('QUOINE', ret.exchange)
        self.assertEqual('BTCUSD', ret.instmt)
        self.assertEqual(1190.7, ret.order_book.b1)
        self.assertEqual(1192.3, ret.order_book.a1)
        self.assertEqual(1.99, ret.order_book.bq1)
        self.assertEqual(6.64, ret.order_book.aq1)
        self.assertEqual(0, ret.last_trade.trade_price)
        self.assertEqual(0, ret.last_trade.trade_volume)
        self.assertEqual(datetime(2017, 4, 7, 0, 0, 48, 770277), data_feed.now())

        # Get snapshot with timeout = 30 mins
        ret = data_feed.get_snapshot(timeout=1000000 * 60 * 30)
        self.assertIsInstance(ret, Snapshot)
        self.assertEqual('GATECOIN', ret.exchange)
        self.assertEqual('BTCHKD', ret.instmt)
        self.assertEqual(9155.9, ret.order_book.b1)
        self.assertEqual(9269.1, ret.order_book.a1)
        self.assertEqual(1.19, ret.order_book.bq1)
        self.assertEqual(5, ret.order_book.aq1)
        self.assertEqual(0, ret.last_trade.trade_price)
        self.assertEqual(0, ret.last_trade.trade_volume)
        self.assertEqual(datetime(2017, 4, 7, 0, 0, 50, 913322), data_feed.now())

        data_feed.disconnect()

if __name__ == '__main__':
    unittest.main()
