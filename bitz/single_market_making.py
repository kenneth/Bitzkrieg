#!/usr/bin/python3
from bitz.exch_gatecoin_eis import ExchGatecoinEis
from bitz.exch_gatecoin_eig import ExchGatecoinEig
from bitz.order_server import OrderServer
from bitz.realtime_strategy import RealTimeStrategy
from bitz.market_data_feed import MarketDataFeed
from bitz.redis_database_client import RedisDatabaseClient
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.logger import ConsoleLogger
from bitz.util import update_fixtime, fixmsg2dict
from datetime import datetime, timedelta
import signal
import argparse
import json

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial
    raise TypeError ("Type not serializable")

class SingleMarketMaking(RealTimeStrategy):
    """
    Single market marking
    """
    def __init__(self, name, ordsvr, logger):
        """
        Constructor
        """
        RealTimeStrategy.__init__(self, name, ordsvr, logger)
        ordsvr.register_strategy(self)
        self.fixed_order_amt = 0.01
        ordsvr.strategy_risk_exposure[self]['open_ask_amt'] = 0
        ordsvr.strategy_risk_exposure[self]['open_bid_amt'] = 0
        ordsvr.strategy_risk_exposure[self]['max_bid_amt'] = self.fixed_order_amt
        ordsvr.strategy_risk_exposure[self]['max_ask_amt'] = self.fixed_order_amt
        self.target_instmt = ('Gatecoin', 'BTCHKD', 0.1)
        self.referenced_instmts = [('Quoine', 'BTCUSD', 7.75, 7.80)]
        self.opened_orders = []
        self.last_status_inquiry_time = datetime.now()

    def register_market_data_feed(self, market_data_feed):
        """
        Register market data feed
        """
        self.market_data_feed = market_data_feed

    def monitor(self):
        """
        Monitor the market
        """
        assert self.market_data_feed is not None, \
                "Market data feed is not registered."

        while True:

            # Exit the loop if clean signal is received
            if len(self.ordsvr.strategy_open_orders[self]) == 0 and not self.running:
                break

            snapshot = self.market_data_feed.get_snapshot(timeout=5000)
            target_exchange = self.target_instmt[0]
            target_instmt = self.target_instmt[1]
            tick_size = self.target_instmt[2]

            # Check strategy
            if snapshot is not None:
                """
                1. Calculate the fair price of the target instrument
                2. If there is no open position, open a new order
                """
                fair_bid_price = 1e9
                fair_ask_price = 0
                cal_instmts = self.referenced_instmts[:]
                cal_instmts += [(target_exchange, \
                                 target_instmt, \
                                 tick_size, \
                                 tick_size)]

                assert target_exchange in self.ordsvr.exchange_risk_exposure.keys(), \
                    "Target instrument %s has not been registered yet." % target_exchange

                target_available_balance = self.ordsvr.exchange_risk_exposure[target_exchange]["AvailableBalance"]
                target_buy_currency = target_instmt[3:]
                target_sell_currency = target_instmt[0:3]
                assert target_buy_currency in target_available_balance.keys(), \
                        "Target buy currency %s is not found in exchange %s" % \
                        (target_buy_currency, target_exchange)
                assert target_sell_currency in target_available_balance.keys(), \
                        "Target sell currency %s is not found in exchange %s" % \
                        (target_sell_currency, target_exchange)
                target_buy_margin = target_available_balance[target_buy_currency]
                target_sell_margin = target_available_balance[target_sell_currency]

                for i in range(0, len(cal_instmts)):
                    referenced = cal_instmts[i]
                    exchange = referenced[0]
                    instmt = referenced[1]
                    bid_rate = referenced[2]
                    ask_rate = referenced[3]
                    if (exchange, instmt) not in self.market_data_feed.snapshots.keys():
                        fair_bid_price = 1e9
                        fair_ask_price = 0
                        break

                    depth = self.market_data_feed.snapshots[(exchange, instmt)].order_book
                    if depth.b1 == 0.0 or depth.a1 == 0.0:
                        fair_bid_price = 1e9
                        fair_ask_price = 0
                        break

                    if i != len(cal_instmts) - 1:
                        fair_bid_price = min(fair_bid_price, depth.b1 * bid_rate)
                        fair_ask_price = max(fair_ask_price, depth.a1 * ask_rate)
                    else:
                        fair_bid_price = min(fair_bid_price, depth.b1 + bid_rate)
                        fair_ask_price = max(fair_ask_price, depth.a1 - ask_rate)

                # self.logger.info(self.__class__.__name__, "FBid = %.6f, FAsk = %.6f" % \
                #                     (fair_bid_price, fair_ask_price))

                for side in [Fix.Tags.Side.Values.BUY, Fix.Tags.Side.Values.SELL]:
                    # Check risk limit
                    if side == Fix.Tags.Side.Values.BUY and \
                       (self.ordsvr.strategy_risk_exposure[self]['open_bid_amt'] >= \
                       self.ordsvr.strategy_risk_exposure[self]['max_bid_amt'] or \
                       fair_bid_price >= 1e9 or \
                       target_buy_margin < fair_bid_price * self.fixed_order_amt):
                        continue
                    elif side == Fix.Tags.Side.Values.SELL and \
                       (self.ordsvr.strategy_risk_exposure[self]['open_ask_amt'] >= \
                       self.ordsvr.strategy_risk_exposure[self]['max_ask_amt'] or \
                       fair_ask_price <= 0 or \
                       target_sell_margin < self.fixed_order_amt):
                        continue

                    # Create an order
                    order_request = Fix.Messages.NewOrderSingle()
                    order_request.Instrument.SecurityExchange.value = self.target_instmt[0]
                    order_request.Instrument.Symbol.value = self.target_instmt[1]
                    order_request.OrderQtyData.OrderQty.value = self.fixed_order_amt
                    order_request.ClOrdID.value = datetime.utcnow().strftime('%Y%m%d%H%M%S%fSMMNEW')
                    order_request.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
                    update_fixtime(order_request, Fix.Tags.SendingTime.Tag)

                    if side == Fix.Tags.Side.Values.BUY:
                        order_request.Side.value = Fix.Tags.Side.Values.BUY
                        order_request.Price.value = int(fair_bid_price / tick_size + tick_size/2) * tick_size
                    else:
                        order_request.Side.value = Fix.Tags.Side.Values.SELL
                        order_request.Price.value = int(fair_ask_price / tick_size + tick_size/2) * tick_size

                    # Send out the request
                    fix_response = self.ordsvr.request(self, order_request)

                    # Append opened orders
                    if fix_response.OrdStatus == Fix.Tags.OrdStatus.Values.NEW:
                        self.opened_orders.append(fix_response)

            """
            If there is opened position, check if
                i. The position is filled => Signal it
                ii. The price of the opened position is out of the range
                    of the fair price => Cancel all opened orders
                iii. Any other orders is,  ahead our orders => Keep the position
                     but raise a notification
                iv. The market data may be staled => Cancel all opened orders
            """

            # Check the order status first
            if len(self.ordsvr.strategy_open_orders[self]) > 0 and \
               datetime.now() - self.last_status_inquiry_time > timedelta(seconds=5):
                self.last_status_inquiry_time = datetime.now()
                mass_order_status = Fix.Messages.OrderMassStatusRequest()
                mass_order_status.MassStatusReqID.value = datetime.utcnow().strftime('%Y%m%d%H%M%S%fSMMSTA')
                mass_order_status.Instrument.SecurityExchange.value = target_exchange
                mass_order_status.Instrument.Symbol.value = target_instmt
                self.ordsvr.request(self, mass_order_status)

            keys = list(self.ordsvr.strategy_open_orders[self].keys())
            for key in keys:
                open_order = self.ordsvr.strategy_open_orders[self][key]
                if datetime.now() - open_order.TransactTime.value > timedelta(seconds=15):
                    # Cancel the order
                    order_request = Fix.Messages.OrderCancelRequest()
                    order_request.Instrument.SecurityExchange.value = open_order.Instrument.SecurityExchange.value
                    order_request.Instrument.Symbol.value = open_order.Instrument.Symbol.value
                    order_request.Side.value = open_order.Side.value
                    order_request.ClOrdID.value = datetime.utcnow().strftime('%Y%m%d%H%M%S%fSMMCNC')
                    order_request.SecondaryClOrdID.value = open_order.SecondaryClOrdID.value
                    order_request.OrderID.value = open_order.OrderID.value
                    update_fixtime(order_request, Fix.Tags.SendingTime.Tag)

                    # Send out the request
                    fix_response = self.ordsvr.request(self, order_request)
                    if fix_response.OrdStatus.value == Fix.Tags.OrdStatus.Values.CANCELED and \
                        fix_response.ExecType.value == Fix.Tags.ExecType.Values.CANCELED:
                        del self.ordsvr.strategy_open_orders[self][key]
                else:
                    # Keep the order
                    pass



    def _update_order_book(self):
        """
        Update order book
        """
        pass

    def _send_order(self, **kargs):
        """
        Send order
        """
        pass

    def _check_open_orders(self, **kargs):
        """
        Check open orders from the order server
        """
        pass

def get_args():
    """
    Get input arguments
    """
    parser = argparse.ArgumentParser(description='Single market marking.')
    parser.add_argument('-config', action='store', dest='config',
                        help='Configuration file path',
                        default='')
    return parser.parse_args()


def main():
    # Get input arguments
    args = get_args()

    # Set configuration
    config = ConfigParser.ConfigParser()
    config.read(args.config)

    # Gateway initialization
    gatecoin_eig = ExchGatecoinEig(ConsoleLogger.static_logger,
                                   config.get('Gatecoin', 'public'),
                                   config.get('Gatecoin', 'private'))
    gatecoin_eis = ExchGatecoinEis(gatecoin_eig)

    # Database initialization
    database_port = int(config.get('Database', 'Port'))
    request_db_client = RedisDatabaseClient()
    request_db_client.connect(host='localhost',
                              port=database_port,
                              db=int(config.get('Database', 'Request')))
    response_db_client = RedisDatabaseClient()
    response_db_client.connect(host='localhost',
                              port=database_port,
                              db=int(config.get('Database', 'Response')))

    # Order server initialization
    ordsvr = OrderServer(request_db_client, response_db_client, ConsoleLogger.static_logger)
    ordsvr.register_gateway('Gatecoin', gatecoin_eis)
    ordsvr.query_risk_exposure()

    # Strategy initialization
    smm = SingleMarketMaking('SingleMarketMaking', ordsvr, ConsoleLogger.static_logger)
    signal.signal(signal.SIGINT, smm.handle_signal)
    signal.signal(signal.SIGTERM, smm.handle_signal)
    market_data_feed = MarketDataFeed(ConsoleLogger.static_logger)
    market_data_feed.connect(addr=config.get('MarketFeed', 'Host'))
    smm.register_market_data_feed(market_data_feed)
    smm.monitor()

if __name__ == '__main__':
    main()
