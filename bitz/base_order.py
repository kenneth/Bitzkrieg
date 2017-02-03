#!/usr/bin/python3  
from util import Side

class BaseOrder(object):
    """
    Base Order
    """
    def __init__(self):
        """
        Constructor
        """
        self.instmt = None
        self.exchange_name = ''
        self.instmt_name = ''
        self.side = Side.NONE
        self.price = 0.0
    