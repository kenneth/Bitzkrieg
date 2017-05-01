#!/usr/bin/python3
from bitz.market_data import Snapshot


class MarketDataFeed:
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
        self.logger = logger
        self.feed = None
        self.snapshots = {}

    def connect(self, **kwargs):
        """
        Connect to the market data feed
        """
        raise NotImplementedError("Please Implement this method")

    def disconnect(self, **kwargs):
        """
        Disconnect to the market data feed
        """
        raise NotImplementedError("Please Implement this method")

    def get_snapshot(self, timeout=100):
        """
        Get snapshot
        """
        # Poll the message
        raise NotImplementedError("Please Implement this method")

    def get_exchange_snapshot(self, exchange, instmt_name) -> Snapshot:
        """
        Get exchange snapshot
        :param exchange: Exchange name
        :param instmt_name: Instrument name
        :return: Exchange snapshot. None if not found
        """
        exchange = exchange.upper()
        instmt_name = instmt_name.upper()
        if (exchange, instmt_name) in self.snapshots.keys():
            return self.snapshots[(exchange, instmt_name)]
        else:
            return None

    def now(self):
        """
        Get the current time
        :return: Current datetime
        """
        raise NotImplementedError("Please Implement this method")

    def now_string(self, format='%Y%m%dT%H:%M:%S.%f'):
        """
        Get the current time in string
        :param format: Time format
        :return: Current datetime in string
        """
        raise NotImplementedError("Please Implement this method")

