#!/usr/bin/python3 
from bitz.exch_gatecoin_eis import ExchGatecoinEis
from bitz.exch_gatecoin_eig import ExchGatecoinEig
from bitz.order_server import OrderServer
from bitz.realtime_strategy import RealTimeStrategy
from bitz.market_data_feed import MarketDataFeed
from bitz.redis_database_client import RedisDatabaseClient
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.logger import ConsoleLogger
from bitz.util import update_sendingtime
from datetime import datetime
import argparse

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
        self.referenced_instmts = [('Bitfinex', 'BTCUSD', 7.75, 7.80)]
        self.opened_orders = []
    
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
            snapshot = self.market_data_feed.get_snapshot()
            
            # Check strategy
            if snapshot is not None:
                """
                1. Calculate the fair price of the target instrument
                2. If there is no open position, open a new order
                """
                target_exchange = self.target_instmt[0]
                target_instmt = self.target_instmt[1]
                tick_size = self.target_instmt[2]
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
                
                self.logger.info('test', "FBid = %.6f, FAsk = %.6f" % (fair_bid_price, fair_ask_price))
                for side in [Fix.Tags.Side.Values.BUY, Fix.Tags.Side.Values.SELL]:
                    # Check risk limit
                    if side == Fix.Tags.Side.Values.BUY and \
                       (self.ordsvr.strategy_risk_exposure[self]['open_bid_amt'] >= \
                       self.ordsvr.strategy_risk_exposure[self]['max_bid_amt'] or \
                       fair_bid_price >= 1e9):
                        continue
                    elif side == Fix.Tags.Side.Values.SELL and \
                       (self.ordsvr.strategy_risk_exposure[self]['open_ask_amt'] >= \
                       self.ordsvr.strategy_risk_exposure[self]['max_ask_amt'] or \
                       fair_ask_price <= 0):
                        continue
                    
                    # Create an order
                    order_request = Fix.Messages.NewOrderSingle()
                    order_request.Instrument.SecurityExchange.value = self.target_instmt[0]
                    order_request.Instrument.Symbol.value = self.target_instmt[1]
                    order_request.OrderQtyData.OrderQty.value = self.fixed_order_amt
                    order_request.ClOrdID.value = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
                    order_request.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
                    update_sendingtime(order_request)
                    
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
    parser.add_argument('-gatecoin_public', action='store', dest='gatecoin_public',
                        help='Gatecoin public API key.',
                        default='')
    parser.add_argument('-gatecoin_private', action='store', dest='gatecoin_private',
                        help='Gatecoin private API key.',
                        default='')                        
    return parser.parse_args()  
    

def main():
    # Get input arguments
    args = get_args()
    
    # Gateway initialization
    gatecoin_eig = ExchGatecoinEig(ConsoleLogger.static_logger,
                                   args.gatecoin_public,
                                   args.gatecoin_private)
    gatecoin_eis = ExchGatecoinEis(gatecoin_eig)
    
    # Database initialization
    request_db_client = RedisDatabaseClient()
    request_db_client.connect(host='localhost', port=6379, db=0)
    response_db_client = RedisDatabaseClient()
    response_db_client.connect(host='localhost', port=6379, db=1)    
    
    # Order server initialization
    ordsvr = OrderServer(request_db_client, response_db_client, ConsoleLogger.static_logger)
    ordsvr.register_gateway('Gatecoin', gatecoin_eis)
    ordsvr.query_risk_exposure()
    
    # Strategy initialization
    smm = SingleMarketMaking('SingleMarketMaking', ordsvr, ConsoleLogger.static_logger)
    market_data_feed = MarketDataFeed(ConsoleLogger.static_logger)
    market_data_feed.connect(addr='tcp://127.0.0.1:6001')
    smm.register_market_data_feed(market_data_feed)
    smm.monitor()
    
if __name__ == '__main__':
    main()