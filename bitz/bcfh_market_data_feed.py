#!/usr/bin/python3
from bitz.market_data_feed import MarketDataFeed
from bitz.market_data import L2Depth, Trade, Snapshot
from bitz.logger import ConsoleLogger
from datetime import datetime
import zmq

class BcfhMarketDataFeed(MarketDataFeed):
    """
    Market data feed
    """
    MAX_WARNING_COUNT = 10

    def __init__(self, logger):
        """
        Constructor
        :param name                     Market data feed name
        :param logger                   Logger
        :param func_recv_data_feed      Function delegate for receiving data feed
        """
        MarketDataFeed.__init__(self, logger)
        self.warning_count = 0

    def connect(self, **kwargs):
        """
        Connect to the market data feed
        """
        addr = kwargs['addr']
        context = zmq.Context()
        self.feed = context.socket(zmq.SUB)
        self.feed.connect(addr)
        self.feed.setsockopt_string(zmq.SUBSCRIBE, '')
        self.poller = zmq.Poller()
        self.poller.register(self.feed, zmq.POLLIN)

    def get_snapshot(self, timeout=100):
        """
        Get snapshot
        """
        # Poll the message
        socks = dict(self.poller.poll(timeout))
        if len(socks) > 0 and socks[self.feed] == zmq.POLLIN:
            data = self.feed.recv_pyobj()
        else:
            return Snapshot.UpdateType.NONE

        # Handle the polled message
        table_name = data['table']
        if table_name == 'exchanges_snapshot':
            assert('exchange' in data.keys())
            assert('instmt' in data.keys())
            exchange = data['exchange'].upper()
            instmt = data['instmt'].upper()
            snapshot = self.snapshots.setdefault((exchange, instmt), Snapshot(exchange, instmt))
            if len(data.keys()) != 28:
                self.logger.error(self.__class__.__name__, "Invalid data (%s)" % data)
                return Snapshot.UpdateType.NONE

            snapshot.update_type = data['update_type']
            if snapshot.update_type == Snapshot.UpdateType.ORDER_BOOK:
                snapshot.order_book.b1 = data['b1']
                snapshot.order_book.b2 = data['b2']
                snapshot.order_book.b3 = data['b3']
                snapshot.order_book.b4 = data['b4']
                snapshot.order_book.b5 = data['b5']
                snapshot.order_book.bq1 = data['bq1']
                snapshot.order_book.bq2 = data['bq2']
                snapshot.order_book.bq3 = data['bq3']
                snapshot.order_book.bq4 = data['bq4']
                snapshot.order_book.bq5 = data['bq5']
                snapshot.order_book.a1 = data['a1']
                snapshot.order_book.a2 = data['a2']
                snapshot.order_book.a3 = data['a3']
                snapshot.order_book.a4 = data['a4']
                snapshot.order_book.a5 = data['a5']
                snapshot.order_book.aq1 = data['aq1']
                snapshot.order_book.aq2 = data['aq2']
                snapshot.order_book.aq3 = data['aq3']
                snapshot.order_book.aq4 = data['aq4']
                snapshot.order_book.aq5 = data['aq5']
                snapshot.order_book.date_time = datetime.strptime(data['order_date_time'],
                                                                  "%Y%m%d %H:%M:%S.%f")
            elif snapshot.update_type == Snapshot.UpdateType.TRADES:
                snapshot.last_trade.trade_price = data['trade_px']
                snapshot.last_trade.trade_volume = data['trade_volume']
                snapshot.last_trade.date_time = datetime.strptime(data['trades_date_time'],
                                                                  "%Y%m%d %H:%M:%S.%f")

            return snapshot

        else:
            self.warning_count += 1
            if self.warning_count > MarketDataFeed.MAX_WARNING_COUNT:
                self.logger.error(self.__class__.__name__, 'Warning:' +
                'Other table name %s has been received.' % table_name)
                self.warning_count = 0

            return Snapshot.UpdateType.NONE

    def now(self):
        """
        Get the current time
        :return: Current datetime
        """
        return datetime.utcnow()

    def now_string(self, format='%Y%m%dT%H:%M:%S.%f'):
        """
        Get the current time in string
        :param format: Time format
        :return: Current datetime in string
        """
        raise datetime.utcnow()

if __name__ == '__main__':
    addr = 'tcp://103.253.147.49:6001'
    mdf = BcfhMarketDataFeed(ConsoleLogger.static_logger)
    mdf.connect(addr=addr)
    while True:
        ss = mdf.get_snapshot(5000)
        print(ss)
