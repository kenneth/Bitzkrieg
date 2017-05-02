#!/bin/python
from bitz.market_data_feed import MarketDataFeed
from bitz.bcfh_market_data_feed import BcfhMarketDataFeed
from bitz.file_market_data_feed import FileMarketDataFeed
from bitz.realtime_database import AbstractRealtimeDatabase, InternalRealtimeDatabase
from bitz.journal_db import AbstractJournalDatabase, InternalJournalDatabase
from bitz.order_server import OrderServer
from bitz.logger import Logger, ConsoleLogger
from bitz.risk_manager import RiskManager
from bitz.exch_backtesting import ExchBacktesting

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

class Factory(object):
    """
    Factory
    """
    def __init__(self, config_path):
        """
        Constructor
        :param config: COnfiguration
        """
        self.__config = ConfigParser.ConfigParser()
        self.__config.read(config_path)

    def create_logger(self) -> Logger:
        """
        Create logger
        :return: logger
        """
        return ConsoleLogger.static_logger

    def create_risk_manager(self) -> RiskManager:
        """
        Create risk manager
        :return: Risk manager
        """
        return RiskManager()

    def create_realtime_database(self) -> AbstractRealtimeDatabase:
        """
        Create realtime database
        :return: Realtime database
        """
        # TODO: Provide more choices
        return InternalRealtimeDatabase()

    def create_journal_database(self) -> AbstractJournalDatabase:
        """
        Create journal database
        :return: Journal database
        """
        # TODO: Provide more choices
        return InternalJournalDatabase()

    def create_market_data_feed(self, logger) -> MarketDataFeed:
        """
        Create market data feed
        :param logger: Logger
        :return: Market data feed
        """
        market_data_feed_type = self.__config.get('MarketFeed', 'Type')
        if market_data_feed_type == 'file':
            market_data_feed = FileMarketDataFeed(logger)
            market_data_feed.connect(files=eval(self.__config.get('MarketFeed', 'Files')))
        elif market_data_feed_type == 'bcfh':
            market_data_feed = BcfhMarketDataFeed(logger)
            market_data_feed.connect(addr=self.__config.get('MarketFeed', 'Host'))
        else:
            raise Exception("Cannot recognize the market data feed type %s" % market_data_feed_type)

        return market_data_feed

    def create_order_server(self, logger, journal_db, realtime_db, risk_manager, market_data_feed):
        """
        Create order server
        :param logger: Logger
        :param journal_db: Journal database
        :param realtime_db: Realtime database
        :param risk_manager: Risk manager
        :param market_data_feed: Market data feed
        :return: Order server
        """
        return OrderServer(logger, journal_db, realtime_db, risk_manager, market_data_feed)

    def create_exchange(self, exchange_name, **kwargs):
        """
        Create exchange
        :param exchange_name: Exchange name
        :param logger: Logger
        :return: Exchange
        """
        market_data_feed_type = self.__config.get('MarketFeed', 'Type')
        is_production = (market_data_feed_type == 'bcfh')

        if is_production:
            raise NotImplementedError("Not yet implemented")
        else:
            market_data_feed = kwargs['market_data_feed']
            latency = kwargs['network_latency'] if 'network_latency' in kwargs.keys() else None
            if latency is None:
                return ExchBacktesting(exchange_name, market_data_feed)
            else:
                return ExchBacktesting(exchange_name, market_data_feed, latency)

