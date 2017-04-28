#!/bin/python
class Instrument:
    """
    Instrument
    """
    def __init__(self, exchange, instmt_name, fiat_rate, tick_size):
        self.exchange = exchange
        self.instmt_name = instmt_name
        self.fiat_rate = fiat_rate
        self.tick_size = tick_size

Gatecoin_BTCHKD = Instrument('Gatecoin', 'BTCHKD', 7.8, 0.01)
Quoine_BTCUSD = Instrument('Quoine', 'BTCUSD', 1, 0.01)
