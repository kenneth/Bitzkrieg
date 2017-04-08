#!/usr/bin/python3
from bitz.market_data_feed import MarketDataFeed
from bitz.market_data import L2Depth, Trade, Snapshot
from bitz.logger import ConsoleLogger
from datetime import datetime, timedelta
import zmq

class FileMarketDataFeed(MarketDataFeed):
    """
    Market data feed
    """
    class FileFields:
        """
        File fields index in a csv file
        """
        Id = 0
        TradePx = 1
        TradeVol = 2
        B1 = 3
        B2 = 4
        B3 = 5
        B4 = 6
        B5 = 7
        A1 = 8
        A2 = 9
        A3 = 10
        A4 = 11
        A5 = 12
        BQ1 = 13
        BQ2 = 14
        BQ3 = 15
        BQ4 = 16
        BQ5 = 17
        AQ1 = 18
        AQ2 = 19
        AQ3 = 20
        AQ4 = 21
        AQ5 = 22
        OrderUpdateTime = 23
        TradeUpdateTime = 24
        UpdateType = 25
        DateTimeFormat = "%Y-%m-%dD%H:%M:%S.%f000"

    class FileHandler:
        """
        File handler
        """
        def __init__(self, fname):
            """
            Constructor
            :param fname    File name
            """
            self.fhandler = open(fname, "r")
            self.exchange = fname.split('_')[1]
            self.instmt_name = fname.split('_')[2]
            self.fhandler.readline()
            self.curr = []
            self.next = self.fhandler.readline().split(',')
            self.curr_datetime = datetime(2000, 1, 1, 0, 0, 0)
            self.next_datetime = datetime(2000, 1, 1, 0, 0, 0)
            self.snapshot = None

        def get_next_line(self):
            """
            Get the next line
            :return: True if the next line has been gotten.
            """
            self.curr = self.next
            self.next = self.fhandler.readline().split(',')

            if len(self.curr) == 26 and len(self.next) == 26:
                # Calculate the curr and next date time. Take the latest of order and trade time.
                curr_order_datetime = datetime.strptime(self.curr[FileMarketDataFeed.FileFields.OrderUpdateTime], FileMarketDataFeed.FileFields.DateTimeFormat)
                next_order_datetime = datetime.strptime(self.next[FileMarketDataFeed.FileFields.OrderUpdateTime], FileMarketDataFeed.FileFields.DateTimeFormat)
                curr_trade_datetime = datetime.strptime(self.curr[FileMarketDataFeed.FileFields.TradeUpdateTime], FileMarketDataFeed.FileFields.DateTimeFormat)
                next_trade_datetime = datetime.strptime(self.next[FileMarketDataFeed.FileFields.TradeUpdateTime], FileMarketDataFeed.FileFields.DateTimeFormat)
                if curr_order_datetime > curr_trade_datetime:
                    self.curr_datetime = curr_order_datetime
                else:
                    self.curr_datetime = curr_trade_datetime

                if next_order_datetime > next_trade_datetime:
                    self.next_datetime = next_order_datetime
                else:
                    self.next_datetime = next_trade_datetime

                return True
            else:
                # Return false if there is no next row
                return False

    @staticmethod
    def __update(snapshot, row):
        """
        Update the snapshot by the row
        :param snapshot:    Snapshot
        :param row:         Row
        """
        snapshot.last_trade.trade_price = row[FileMarketDataFeed.FileFields.TradePx]
        snapshot.last_trade.trade_volume = row[FileMarketDataFeed.FileFields.TradeVol]
        snapshot.order_book.b1 = row[FileMarketDataFeed.FileFields.B1]
        snapshot.order_book.b2 = row[FileMarketDataFeed.FileFields.B2]
        snapshot.order_book.b3 = row[FileMarketDataFeed.FileFields.B3]
        snapshot.order_book.b4 = row[FileMarketDataFeed.FileFields.B4]
        snapshot.order_book.b5 = row[FileMarketDataFeed.FileFields.B5]
        snapshot.order_book.a1 = row[FileMarketDataFeed.FileFields.A1]
        snapshot.order_book.a2 = row[FileMarketDataFeed.FileFields.A2]
        snapshot.order_book.a3 = row[FileMarketDataFeed.FileFields.A3]
        snapshot.order_book.a4 = row[FileMarketDataFeed.FileFields.A4]
        snapshot.order_book.a5 = row[FileMarketDataFeed.FileFields.A5]
        snapshot.order_book.bq1 = row[FileMarketDataFeed.FileFields.BQ1]
        snapshot.order_book.bq2 = row[FileMarketDataFeed.FileFields.BQ2]
        snapshot.order_book.bq3 = row[FileMarketDataFeed.FileFields.BQ3]
        snapshot.order_book.bq4 = row[FileMarketDataFeed.FileFields.BQ4]
        snapshot.order_book.bq5 = row[FileMarketDataFeed.FileFields.BQ5]
        snapshot.order_book.aq1 = row[FileMarketDataFeed.FileFields.AQ1]
        snapshot.order_book.aq2 = row[FileMarketDataFeed.FileFields.AQ2]
        snapshot.order_book.aq3 = row[FileMarketDataFeed.FileFields.AQ3]
        snapshot.order_book.aq4 = row[FileMarketDataFeed.FileFields.AQ4]
        snapshot.order_book.aq5 = row[FileMarketDataFeed.FileFields.AQ5]
        snapshot.last_trade.date_time = datetime.strptime(row[FileMarketDataFeed.FileFields.TradeUpdateTime], FileMarketDataFeed.FileFields.DateTimeFormat)
        snapshot.order_book.date_time = datetime.strptime(row[FileMarketDataFeed.FileFields.OrderUpdateTime], FileMarketDataFeed.FileFields.DateTimeFormat)

    def __init__(self, logger):
        """
        Constructor
        :param name                     Market data feed name
        :param logger                   Logger
        :param func_recv_data_feed      Function delegate for receiving data feed
        """
        MarketDataFeed.__init__(self, logger)
        self.file_handlers = []
        self.__now = datetime(2000, 1, 1, 0, 0, 0)

    def connect(self, **kwargs):
        """
        Connect to the market data feed
        """
        files=kwargs['files']

        # Initialise the file handlers first
        for file_name in files:
            file_handler = FileMarketDataFeed.FileHandler(file_name)
            snapshot = self.snapshots.setdefault((file_handler.exchange, file_handler.instmt_name),
                                                 Snapshot(file_handler.exchange, file_handler.instmt_name))
            file_handler.snapshot = snapshot
            if file_handler.get_next_line():
                FileMarketDataFeed.__update(snapshot, file_handler.curr)
                # print("Name:%s\n%s\n%s\n%s\n%s\n" % (file_name, file_handler.curr_datetime, file_handler.next_datetime, file_handler.curr, file_handler.next))
            else:
                raise Exception("Cannot get the next line on the file %s" % file_name)

            self.file_handlers.append(file_handler)

        # For each file_handler, roll the cursor to a time that the next time must be larger than the time 'now'
        while True:
            is_complete = True
            for file_handler in self.file_handlers:
                if file_handler.next_datetime < self.__last_update_time():
                    is_complete = False
                    if file_handler.get_next_line():
                        FileMarketDataFeed.__update(snapshot, file_handler.curr)
                        # print("Name:%s\n%s\n%s\n%s\n%s\n" % (file_name, file_handler.curr_datetime, file_handler.next_datetime, file_handler.curr, file_handler.next))
                    else:
                        raise Exception("Cannot get the next line on the file %s/%s at now (%s)" % \
                                        (file_handler.exchange, file_handler.instmt_name, self.__last_update_time()))

            if is_complete:
                break

        # Update the current time as the last update time
        self.__now = self.__last_update_time()
        return True

    def get_snapshot(self, timeout=100):
        """
        Get snapshot
        """
        # Poll the message
        if self.__now + timedelta(microseconds=timeout) < self.__next_update_time()[1]:
            self.__now = self.__now + timedelta(microseconds=timeout)
            return Snapshot.UpdateType.NONE
        else:
            next_filehandler, next_update_time = self.__next_update_time()
            # Roll the next line
            if next_filehandler.get_next_line():
                FileMarketDataFeed.__update(next_filehandler.snapshot, next_filehandler.curr)
                self.__now = next_update_time
                return next_filehandler.snapshot
            else:
                # Request to terminate
                return None

    def now(self):
        """
        Get the current time
        :return: Current datetime
        """
        return self.__now

    def __last_update_time(self):
        """
        Get the last update time of all instruments
        :return: The last update datetime
        """
        curr_datetime = datetime(2000, 1, 1, 0, 0, 0)
        for file_handler in self.file_handlers:
            if file_handler.curr_datetime > curr_datetime:
                curr_datetime = file_handler.curr_datetime

        return curr_datetime

    def __next_update_time(self):
        """
        Get the next update time of all instruments
        :return: The next update file_handler and datetime. None if no file handlers
        """
        if len(self.file_handlers) == 0:
            return None
        else:
            next_filehandler = self.file_handlers[0]
            next_datetime = self.file_handlers[0].next_datetime
            for file_handler in self.file_handlers:
                if file_handler.next_datetime < next_datetime:
                    next_filehandler = file_handler
                    next_datetime = file_handler.next_datetime

            return next_filehandler, next_datetime


if __name__ == '__main__':
    market_data_feed = FileMarketDataFeed(ConsoleLogger.static_logger)
    market_data_feed.connect(files=['test\\exch_quoine_btchkd_snapshot_20170406.csv',
                                    'test\\exch_bitmex_xbtusd_snapshot_20170406.csv'])
    while True:
        snapshot = market_data_feed.get_snapshot(timeout=10000)
        if snapshot is None:
            break
        elif isinstance(snapshot, Snapshot):
            print('%s/%s: %s' % (snapshot.exchange, snapshot.instmt, snapshot.order_book.values()))
