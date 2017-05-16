#!/bin/python
class Instrument:
    """
    Instrument
    """
    def __init__(self, exchange, instmt_name, usd_rate, price_min_size, qty_min_size):
        self.exchange = exchange
        self.instmt_name = instmt_name
        self.usd_rate = usd_rate
        self.price_min_size = price_min_size
        self.qty_min_size = qty_min_size

class InstrumentList:
    """
    Instrument list
    """
    def __init__(self):
        self.__list = {}        # Key with tuple (exchange, instmt), value with Instrument

    def get(self, exchange, instmt_name) -> Instrument:
        """
        Get the instrument
        :param exchange: Exchange name
        :param instmt_name: Instrument name
        :return: Instrument
        """
        exchange = exchange.upper()
        instmt_name = instmt_name.upper()
        assert (exchange, instmt_name) in self.__list.keys(), "Cannot find the instmt (%s/%s)." % (exchange, instmt_name)
        return self.__list[(exchange, instmt_name)]

    def insert(self, instmt: Instrument):
        """
        Insert the instrument
        :param instmt: Instrument
        """
        exchange = instmt.exchange.upper()
        instmt_name = instmt.instmt_name.upper()
        assert (exchange, instmt_name) not in self.__list.keys(), "Duplicated instmt (%s/%s)." % (exchange, instmt_name)
        self.__list[(exchange, instmt_name)] = instmt
