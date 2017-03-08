#!/usr/bin/python3 
class RealTimeStrategy:
    """
    Real time strategy.
    
    The strategy handles the following:
    1. Subscribe the market data feed
    2. Manage the exchange price depth and trades
    3. Trigger orders to order server
    4. Maintain orders
    5. Risk management
    """
    def __init__(self, name, ordsvr, logger):
        """
        Constructor
        """
        self.name = name                # Strategy name
        self.ordsvr = ordsvr      # Order server
        self.logger = logger            # Logger
        self.market_data_feed = None    # Market data feed
        
    def get_name(self):
        """
        Get name
        """
        return self.name
    
    def monitor(self):
        """
        Monitor the market
        """
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
    
    
    
    
    