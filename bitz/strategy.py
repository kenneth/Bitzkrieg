#!/usr/bin/python3 
class Strategy:
    """
    Strategy
    """
    def __init__(self):
        """
        Constructor
        """
    
    def open_orders(self, curr_time, snapshots, updated_snapshot):
        """
        Open orders
        : param curr_time                   Current time in UTC
        : param snapshots                   All the instrument snapshots
        : param updated_snapshot            Updated snapshot
        : return List of orders to open
        """
        return []
    
    def close_orders(self, curr_time, orders, snapshots):
        """
        Close orders
        : param curr_time                   Current time in UTC
        : param orders                      All the orders
        : param snapshots                   All the instrument snapshots
        """
        pass
    