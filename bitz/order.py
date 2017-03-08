#!/usr/bin/python3 
from datetime import datetime


class Side:
    """
    Side
    """
    BUY = 1
    SELL = 2
    
    
class Order:
    """
    Order
    """
    def __init__(self):
        """
        Constructor
        """        
        self.exchange = None
        self.instmt = None
        self.price = 0.0
        self.qty = 0.0
        self.qty_done = 0.0
        self.side = None
        self.date_time = datetime.utcnow()
        self.request_msg = None
        self.strategy = None
    
    def __init__(self, strategy, fix_msg):
        """
        Constructor
        """
        self.strategy = strategy
        self.request_req = fix_msg
        self.exchange = self.request_req.Instrument.SecurityExchange.value
        self.instmt= self.request_req.Instrument.Symbol.value
        self.price = self.request_req.Price.value
        self.qty = self.request_req.OrderQtyData.OrderQty.value
        self.qty_done = 0.0
        self.side = self.request_req.Side.value
        self.date_time = datetime.utcnow()
        
    def to_dict(self):
        return { 'date_time': self.date_time.strftime("%Y%m%d %H:%M:%S.%f"),
                 'exchange': self.exchange,
                 'instmt': self.instmt,
                 'price': self.price,
                 'qty': self.qty,
                 'qty_done': self.qty_done,
                 'side': self.side,
                }
        