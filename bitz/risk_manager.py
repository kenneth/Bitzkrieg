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

    def __init__(self, instmt_list):
        """
        Constructor
        """
        self.__exchanges = {}
        self.__instmt_list = instmt_list

    def register_exchange(self, exchange):
        """
        Register exchange
        :param exchange: Exchange name
        """
        exchange = exchange.upper()
        assert exchange not in self.__exchanges.keys(), "Exchange %s has been registered already." % exchange
        return self.__exchanges.setdefault(exchange, {})

    def get_exchange_balance(self, exchange, currency="") -> Union[RiskLevel, Mapping[str, RiskLevel]]:
        """
        Get exchange balance
        :param currency: Currency
        :return:
        """
        exchange = exchange.upper()
        assert exchange in self.__exchanges.keys()
        if currency == "":
            return self.__exchanges[exchange]
        else:
            currency = currency.upper()
            assert currency in self.__exchanges[exchange].keys()
            return self.__exchanges[exchange][currency]

    def risk_check(self, message: Fix.Messages.NewOrderSingle):
        """
        Risk checking on the exchange
        :param message: New order single
        :return: True if passed.
        """
        assert message.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE, \
                "MsgType %s is not new order single" % message.MsgType
        exchange = message.Instrument.SecurityExchange.value.upper()
        instmt = self.__instmt_list.get(message.Instrument.SecurityExchange.value, message.Instrument.Symbol.value)
        assert exchange in self.__exchanges.keys(), "No exchange %s is defined" % exchange
        assert instmt.quote_currency in self.__exchanges[exchange].keys(), \
                "No currency %s is defined in exchange %s" % (instmt.quote_currency, exchange)
        assert instmt.base_currency in self.__exchanges[exchange].keys(), \
            "No currency %s is defined in exchange %s" % (instmt.base_currency, exchange)
        if message.Side.value == Fix.Tags.Side.Values.BUY:
            exch_fiat_available = self.__exchanges[exchange][instmt.base_currency].available_balance
            fiat_risk = message.Price.value * message.OrderQtyData.OrderQty.value
            return fiat_risk < exch_fiat_available
        elif message.Side.value == Fix.Tags.Side.Values.SELL:
            exch_digital_available = self.__exchanges[exchange][instmt.quote_currency].available_balance
            digital_risk = message.OrderQtyData.OrderQty.value
            return digital_risk < exch_digital_available
        else:
            raise NotImplementedError("Side %s not implemented." % message.Side.value)

    def update_risk_exposure_by_message(self, message, risklevels):
        """
        Update risk exposure by message
        :param message: FIX message
        :param risklevels: Map of risk levels
        """
        if message.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            instmt = self.__instmt_list.get(message.Instrument.SecurityExchange.value, message.Instrument.Symbol.value)
            assert instmt.quote_currency in risklevels.keys(), "Cannot find currency %s" % instmt.quote_currency
            assert instmt.base_currency in risklevels.keys(), "Cannot find currency %s" % instmt.base_currency
            side = message.Side.value
            price = message.Price.value
            qty = message.OrderQtyData.OrderQty.value

            # Deduce the available balance
            if side == Fix.Tags.Side.Values.BUY:
                risklevels[instmt.base_currency].available_balance -= price * qty
            elif side == Fix.Tags.Side.Values.SELL:
                risklevels[instmt.quote_currency].available_balance -= qty
            else:
                raise NotImplementedError("Side has not yet been implemented." % side)
        elif message.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
            instmt = self.__instmt_list.get(message.Instrument.SecurityExchange.value, message.Instrument.Symbol.value)
            assert instmt.quote_currency in risklevels.keys(), "Cannot find currency %s" % instmt.quote_currency
            assert instmt.base_currency in risklevels.keys(), "Cannot find currency %s" % instmt.base_currency
            execType = message.ExecType.value
            if execType == Fix.Tags.ExecType.Values.REJECTED:
                side = message.Side.value
                price = message.Price.value
                qty = message.OrderQtyData.OrderQty.value

                # Revert the available balance
                if side == Fix.Tags.Side.Values.BUY:
                    risklevels[instmt.base_currency].available_balance += price * qty
                elif side == Fix.Tags.Side.Values.SELL:
                    risklevels[instmt.quote_currency].available_balance += qty
                else:
                    raise NotImplementedError("Side has not yet been implemented." % side)
            elif execType == Fix.Tags.ExecType.Values.TRADE:
                side = message.Side.value
                price = message.LastPx.value
                qty = message.LastQty.value

                # Adjust the balance
                if side == Fix.Tags.Side.Values.BUY:
                    risklevels[instmt.base_currency].balance -= price * qty
                    risklevels[instmt.quote_currency].available_balance += qty
                    risklevels[instmt.quote_currency].balance += qty
                elif side == Fix.Tags.Side.Values.SELL:
                    risklevels[instmt.base_currency].available_balance += price * qty
                    risklevels[instmt.base_currency].balance += price * qty
                    risklevels[instmt.quote_currency].balance -= qty
            elif execType == Fix.Tags.ExecType.Values.ORDER_STATUS:
                if message.LeavesQty.value == 0:
                    side = message.Side.value
                    price = message.AvgPx.value
                    qty = message.CumQty.value
                    unfilled_qty = message.OrderQtyData.OrderQty.value - message.CumQty.value

                    # Update the balance when the order is completed
                    if side == Fix.Tags.Side.Values.BUY:
                        risklevels[instmt.base_currency].balance -= price * qty
                        risklevels[instmt.base_currency].available_balance += message.Price.value * unfilled_qty
                        risklevels[instmt.quote_currency].available_balance += qty
                        risklevels[instmt.quote_currency].balance += qty
                    elif side == Fix.Tags.Side.Values.SELL:
                        risklevels[instmt.base_currency].available_balance += price * qty
                        risklevels[instmt.base_currency].balance += price * qty
                        risklevels[instmt.quote_currency].balance -= qty
                        risklevels[instmt.quote_currency].available_balance += unfilled_qty
            elif execType in [Fix.Tags.ExecType.Values.CANCELED,
                              Fix.Tags.ExecType.Values.EXPIRED,
                              Fix.Tags.ExecType.Values.DONE_FOR_DAY,
                              Fix.Tags.ExecType.Values.SUSPENDED]:
                side = message.Side.value
                price = message.Price.value
                qty = message.OrderQtyData.OrderQty.value - message.CumQty.value

                # Revert the remaining qty on the available balance
                if side == Fix.Tags.Side.Values.BUY:
                    risklevels[instmt.base_currency].available_balance += price * qty
                elif side == Fix.Tags.Side.Values.SELL:
                    risklevels[instmt.quote_currency].available_balance += qty
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
                                 Fix.Tags.MsgType.Values.ORDERMASSCANCELREQUEST,
                                 Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST]:
            # Ignore message
            pass
        else:
            raise NotImplementedError("Message type %s has not yet been implemented" % message.MsgType)

