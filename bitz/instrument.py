#!/bin/python
class Instrument:
    """
    Instrument
    """
    def __init__(self, **kwargs):
        self.exchange = kwargs["exchange"]
        self.instmt_name = kwargs["instmt_name"]
        self.usd_rate = kwargs["usd_rate"]
        self.price_min_size = kwargs["price_min_size"]
        self.qty_min_size = kwargs["qty_min_size"]
        self.base_currency = kwargs["base_currency"]
        self.quote_currency = kwargs["quote_currency"]

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
