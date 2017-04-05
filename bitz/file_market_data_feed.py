#!/usr/bin/python3
from bitz.market_data_feed import MarketDataFeed
from bitz.market_data import L2Depth, Trade, Snapshot
from datetime import datetime
import zmq

class FileMarketDataFeed(MarketDataFeed):
    """
    Market data feed
    """

    def __init__(self, logger):
        """
        Constructor
        :param name                     Market data feed name
        :param logger                   Logger
        :param func_recv_data_feed      Function delegate for receiving data feed
        """
        MarketDataFeed.__init__(self, logger)

    def connect(self, **kwargs):
        """
        Connect to the market data feed
        """
        pass

    def get_snapshot(self, timeout=100):
        """
        Get snapshot
        """
        # Poll the message
        pass

