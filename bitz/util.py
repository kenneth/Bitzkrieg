#!/usr/bin/python3  
class Side:
    """
    Side
    """
    NONE = 0
    BUY = 1
    SELL = 2
    
class RequestCode:
    """
    Request Code
    """
    NONE = 0
    ADD_ORDER = 'A'
    AMEND_ORDER = 'M'
    DELETE_ORDER = 'D'