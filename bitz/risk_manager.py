#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix
from typing import Union, Mapping

class RiskManager(object):
    """
    Risk manager
    """
    class RiskLevel(object):
        """
        Risk level
        """
        def __init__(self, name, balance=0, available_balance=0):
            """
            Constructor
            :param name:
            :param balance: Balance
            :param available_balance: Available balance
            """
            self.name = name
            self.balance = balance
            self.available_balance = available_balance

    def __init__(self):
        """
        Constructor
        """
        self.__exchange = {}

    def register_exchange(self, exchange):
        """
        Register exchange
        :param exchange: Exchange name
        """
        exchange = exchange.upper()
        assert exchange not in self.__exchange.keys(), "Exchange %s has been registered already." % exchange
        return self.__exchange.setdefault(exchange, {})

    def get_exchange_balance(self, exchange, currency="") -> Union[RiskLevel, Mapping[str, RiskLevel]]:
        """
        Get exchange balance
        :param currency: Currency
        :return:
        """
        exchange = exchange.upper()
        assert exchange in self.__exchange.keys()
        if currency == "":
            return self.__exchange[exchange]
        else:
            currency = currency.upper()
            assert currency in self.__exchange[exchange].keys()
            return self.__exchange[exchange][currency]

    @staticmethod
    def update_risk_exposure_by_message(message, risklevels):
        """
        Update risk exposure by message
        :param message: FIX message
        :param risklevels: Map of risk levels
        """
        if message.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            instmt = message.Instrument.Symbol.value.upper()
            digital_currency = instmt[0:3]
            fiat_currency = instmt[3:]
            assert digital_currency in risklevels.keys(), "Cannot find currency %s" % digital_currency
            assert fiat_currency in risklevels.keys(), "Cannot find currency %s" % fiat_currency
            side = message.Side.value
            price = message.Price.value
            qty = message.OrderQtyData.OrderQty.value

            # Deduce the available balance
            if side == Fix.Tags.Side.Values.BUY:
                risklevels[fiat_currency].available_balance -= price * qty
            elif side == Fix.Tags.Side.Values.SELL:
                risklevels[digital_currency].available_balance -= qty
            else:
                raise NotImplementedError("Side has not yet been implemented." % side)
        elif message.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
            instmt = message.Instrument.Symbol.value.upper()
            digital_currency = instmt[0:3]
            fiat_currency = instmt[3:]
            assert digital_currency in risklevels.keys(), "Cannot find currency %s" % digital_currency
            assert fiat_currency in risklevels.keys(), "Cannot find currency %s" % fiat_currency
            execType = message.ExecType.value
            if execType == Fix.Tags.ExecType.Values.REJECTED:
                side = message.Side.value
                price = message.Price.value
                qty = message.OrderQtyData.OrderQty.value

                # Revert the available balance
                if side == Fix.Tags.Side.Values.BUY:
                    risklevels[fiat_currency].available_balance += price * qty
                elif side == Fix.Tags.Side.Values.SELL:
                    risklevels[digital_currency].available_balance += qty
                else:
                    raise NotImplementedError("Side has not yet been implemented." % side)
            elif execType == Fix.Tags.ExecType.Values.TRADE:
                side = message.Side.value
                price = message.LastPx.value
                qty = message.LastQty.value

                # Adjust the balance
                if side == Fix.Tags.Side.Values.BUY:
                    risklevels[fiat_currency].balance -= price * qty
                    risklevels[digital_currency].available_balance += qty
                    risklevels[digital_currency].balance += qty
                elif side == Fix.Tags.Side.Values.SELL:
                    risklevels[fiat_currency].available_balance += price * qty
                    risklevels[fiat_currency].balance += price * qty
                    risklevels[digital_currency].balance -= qty
                else:
                    raise NotImplementedError("Side has not yet been implemented." % side)
            elif execType in [Fix.Tags.ExecType.Values.CANCELED,
                              Fix.Tags.ExecType.Values.EXPIRED,
                              Fix.Tags.ExecType.Values.DONE_FOR_DAY,
                              Fix.Tags.ExecType.Values.SUSPENDED]:
                side = message.Side.value
                price = message.Price.value
                qty = message.OrderQtyData.OrderQty.value - message.CumQty.value

                # Revert the remaining qty on the available balance
                if side == Fix.Tags.Side.Values.BUY:
                    risklevels[fiat_currency].available_balance += price * qty
                elif side == Fix.Tags.Side.Values.SELL:
                    risklevels[digital_currency].available_balance += qty
                else:
                    raise NotImplementedError("Side has not yet been implemented." % side)
        elif message.MsgType == Fix.Tags.MsgType.Values.POSITIONREPORT:
            # Update all the currency balance and available balance
            for position in message.PositionAmountData.groups:
                currency = position.PositionCurrency.value.upper()
                value = position.PosAmt.value
                type = position.PosAmtType.value

                if currency not in risklevels:
                    risklevels[currency] = RiskManager.RiskLevel(currency)

                if type == Fix.Tags.PosAmtType.Values.CASH_AMOUNT:
                    risklevels[currency].balance = value
                elif type == Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT:
                    risklevels[currency].available_balance = value
                else:
                    assert False, "Invalid position amount type %d" % type
        elif message.MsgType in [Fix.Tags.MsgType.Values.ORDERCANCELREPLACEREQUEST,
                                 Fix.Tags.MsgType.Values.ORDERCANCELREQUEST,
                                 Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS,
                                 Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST,
                                 Fix.Tags.MsgType.Values.ORDERMASSCANCELREQUEST]:
            # Ignore message
            pass
        else:
            raise NotImplementedError("Message type %s has not yet been implemented" % message.MsgType)

