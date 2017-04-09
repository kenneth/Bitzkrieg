#!/usr/bin/python3
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

    def now(self):
        """
        Get the current time
        :return: Current datetime
        """
        raise NotImplementedError("Please Implement this method")


