#!/bin/python
from bitz.market_data_feed import MarketDataFeed
from bitz.bcfh_market_data_feed import BcfhMarketDataFeed
from bitz.file_market_data_feed import FileMarketDataFeed
from bitz.realtime_database import AbstractRealtimeDatabase, InternalRealtimeDatabase, SqliteRealtimeDatabase
from bitz.journal_database import AbstractJournalDatabase, InternalJournalDatabase
from bitz.order_server import OrderServer
from bitz.logger import Logger, ConsoleLogger
from bitz.risk_manager import RiskManager
from bitz.exch_backtesting import ExchBacktesting
from bitz.instrument import Instrument, InstrumentList
from datetime import datetime
import signal
import os

# Exchanges
from bitz.exch_gatecoin_eig import ExchGatecoinEig
from bitz.exch_gatecoin_eis import ExchGatecoinEis
from bitz.exch_bitmex import ExchBitmex

# Strategies
from bitz.single_market_making import SingleMarketMaking

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
        db = None
        section = 'RealtimeDatabase'
        database_type = self.__config.get(section, 'Type')
        if database_type == 'Internal':
            path = self.__config.get(section, 'Path')
            db = InternalRealtimeDatabase()
            db.connect(path=path)
        elif database_type == 'Sqlite':
            path = self.__config.get(section, 'Path')
            path = os.path.join(path,
                                'realtime_db_%s.db' % datetime.utcnow().strftime("%Y%m%d%H%M%S%f"))
            db = SqliteRealtimeDatabase()
            db.connect(path=path)
        else:
            raise NotImplementedError("Database type (%s) has not yet been implemented." % database_type)

        return db

    def create_journal_database(self) -> AbstractJournalDatabase:
        """
        Create journal database
        :return: Journal database
        """
        section = 'JournalDatabase'
        database_type = self.__config.get(section, 'Type')
        if database_type == 'Internal':
            path = self.__config.get(section, 'Path')
            db = InternalJournalDatabase()
            db.connect(path=path)
            return db
        else:
            raise NotImplementedError("Database type (%s) has not yet been implemented." % database_type)

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

    def create_exchange(self, exchange_name, logger, **kwargs):
        """
        Create exchange
        :param exchange_name: Exchange name
        :param logger: Logger
        :return: Exchange
        """
        market_data_feed_type = self.__config.get('MarketFeed', 'Type')
        is_production = (market_data_feed_type == 'bcfh')

        if is_production:
            if exchange_name in self.__config.sections():
                if exchange_name == 'Gatecoin':
                    public_key = self.__config.get(exchange_name, 'public')
                    private_key = self.__config.get(exchange_name, 'private')
                    eig = ExchGatecoinEig(key=public_key, secret=private_key, logger=logger)
                    eis = ExchGatecoinEis(eig)
                    return eis
                elif exchange_name == 'BitMEX':
                    public_key = self.__config.get(exchange_name, 'public')
                    private_key = self.__config.get(exchange_name, 'private')
                    return ExchBitmex(logger=logger, public_key=public_key, private_key=private_key)
                else:
                    raise NotImplementedError("Exchange (%s) not yet implemented." % exchange_name)
            else:
                raise NotImplementedError("Exchange (%s) not found in the config file." % exchange_name)
        else:
            market_data_feed = kwargs['market_data_feed']
            latency = kwargs['network_latency'] if 'network_latency' in kwargs.keys() else None
            if latency is None:
                return ExchBacktesting(exchange_name, market_data_feed)
            else:
                return ExchBacktesting(exchange_name, market_data_feed, latency)

    def create_instrument_list(self):
        """
        Create instrument list
        :return:
        """
        keyword = 'Instrument.'
        sections = self.__config.sections()
        instmt_list = InstrumentList()
        for section in sections:
            if keyword in section:
                exchange = self.__config.get(section, 'Exchange')
                instmt_name = self.__config.get(section, 'Name')
                usd_rate = float(self.__config.get(section, 'USDRate'))
                price_min_size = float(self.__config.get(section, 'PriceMinSize'))
                qty_min_size = float(self.__config.get(section, 'QtyMinSize'))

                instmt = Instrument(exchange, instmt_name, usd_rate, price_min_size, qty_min_size)
                instmt_list.insert(instmt)

        return instmt_list

    def create_strategies(self, ordsvr: OrderServer, logger: Logger, instmt_list: InstrumentList):
        """
        Create strategies
        :return:
        """
        keyword = 'Strategy.'
        sections = self.__config.sections()
        strategy_list = []
        for section in sections:
            if keyword in section:
                name = self.__config.get(section, 'Name')
                if name == 'SingleMarketMaking':
                    smm = self.__setup_smm(section, ordsvr, logger, instmt_list)
                    strategy_list.append(smm)
                else:
                    raise NotImplementedError("Strategy (%s) not yet implemented." % name)

        return strategy_list

    def __setup_smm(self, section, ordsvr, logger, instmt_list: InstrumentList):
        """
        Setup single market making strategy
        :return: Single market making strategy
        """
        # Target and referenced instruments
        target_instmt_raw = eval(self.__config.get(section, 'TargetInstmt'))
        referenced_instmt_raw = eval(self.__config.get(section, 'ReferencedInstmt'))
        target_instmt = instmt_list.get(target_instmt_raw[0], target_instmt_raw[1])
        referenced_instmt = []
        for exchange, instmt_name in referenced_instmt_raw:
            referenced_instmt.append(instmt_list.get(exchange, instmt_name))

        # Create strategy
        smm = SingleMarketMaking('SingleMarketMaking.%s.%s' % (target_instmt.exchange, target_instmt.instmt_name),
                                 ordsvr, logger, target_instmt, referenced_instmt)

        # Initialise parameters
        param = self.__config.get(section, 'profit_margin_fiat_currency')
        if param != '':
            smm.init_parameters(profit_margin_fiat_currency=int(param))

        param = self.__config.get(section, 'aggressiveness')
        if param != '':
            smm.init_parameters(aggressiveness=int(param))

        param = self.__config.get(section, 'max_rejected_request')
        if param != '':
            smm.init_parameters(max_rejected_request=int(param))

        param = self.__config.get(section, 'market_data_stalled_time_sec')
        if param != '':
            smm.init_parameters(market_data_stalled_time_sec=int(param))

        param = self.__config.get(section, 'default_trading_qty')
        if param != '':
            smm.init_parameters(default_trading_qty=float(param))

        param = self.__config.get(section, 'default_trade_side')
        if param != '':
            smm.init_parameters(default_trade_side=int(param))

        # Signal handling
        signal.signal(signal.SIGINT, smm.handle_signal)
        signal.signal(signal.SIGTERM, smm.handle_signal)

        return smm



