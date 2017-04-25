#!/bin/python
from bitz.risk_manager import RiskManager
from bitz.logger import ConsoleLogger
from bitz.FIX50SP2 import FIX50SP2 as Fix
import unittest
import os

class TRiskManager(unittest.TestCase):
    exchange_name = 'quoine'
    instmt = 'btcusd'
    price = 1200
    qty = 1.5

    @staticmethod
    def __create_position_report() -> Fix.Messages.PositionReport:
        """
        Create position report
        :return: Position report message
        """
        message = Fix.Messages.PositionReport()
        message.Instrument.Symbol = TRiskManager.instmt
        message.Instrument.SecurityExchange = TRiskManager.exchange_name

        for currency, total_balance, available_balance in \
                [('USD', 2000, 2000),
                 ('HKD', 10000, 10000),
                 ('BTC', 1, 1)]:
            # Total
            positionAmountData = Fix.Components.PositionAmountData.NoPosAmt()
            positionAmountData.PositionCurrency.value = currency
            positionAmountData.PosAmt.value = total_balance
            positionAmountData.PosAmtType.value = Fix.Tags.PosAmtType.Values.CASH_AMOUNT
            message.PositionAmountData.groups.append(positionAmountData)

            # Available
            positionAmountData = Fix.Components.PositionAmountData.NoPosAmt()
            positionAmountData.PositionCurrency.value = currency
            positionAmountData.PosAmt.value = available_balance
            positionAmountData.PosAmtType.value = Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT
            message.PositionAmountData.groups.append(positionAmountData)

        return message

    @staticmethod
    def __create_new_order_single() -> Fix.Messages.NewOrderSingle:
        """
        Create a new order single
        :return: New order single
        """
        new_order_single = Fix.Messages.NewOrderSingle()
        side = Fix.Tags.Side.Values.BUY
        new_order_single.Instrument.Symbol.value = TRiskManager.instmt
        new_order_single.Instrument.SecurityExchange.value = TRiskManager.exchange_name
        new_order_single.Price.value = TRiskManager.price
        new_order_single.TriggeringInstruction.TriggerPrice.value = TRiskManager.price
        new_order_single.Side.value = side
        new_order_single.ClOrdID.value = 'NewSingle%.6f' % TRiskManager.price
        new_order_single.OrderQtyData.OrderQty.value = TRiskManager.qty
        new_order_single.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        new_order_single.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY

        return new_order_single

    @staticmethod
    def __create_order_reject() -> Fix.Messages.ExecutionReport:
        """
        Create order reject
        :return: Order reject
        """
        order_reject = Fix.Messages.ExecutionReport()
        side = Fix.Tags.Side.Values.BUY
        order_reject.Instrument.Symbol.value = TRiskManager.instmt
        order_reject.Instrument.SecurityExchange.value = TRiskManager.exchange_name
        order_reject.Price.value = TRiskManager.price
        order_reject.Side.value = side
        order_reject.ClOrdID.value = 'NewSingle%.6f' % TRiskManager.price
        order_reject.OrderQtyData.OrderQty.value = TRiskManager.qty
        order_reject.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        order_reject.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY
        order_reject.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
        order_reject.ExecType.value = Fix.Tags.ExecType.Values.REJECTED

        return order_reject

    @staticmethod
    def __create_order_ack() -> Fix.Messages.ExecutionReport:
        """
        Create order reject
        :return: Order reject
        """
        order_ack = Fix.Messages.ExecutionReport()
        side = Fix.Tags.Side.Values.BUY
        order_ack.Instrument.Symbol.value = TRiskManager.instmt
        order_ack.Instrument.SecurityExchange.value = TRiskManager.exchange_name
        order_ack.Price.value = TRiskManager.price
        order_ack.Side.value = side
        order_ack.ClOrdID.value = 'NewSingle%.6f' % TRiskManager.price
        order_ack.OrderQtyData.OrderQty.value = TRiskManager.qty
        order_ack.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        order_ack.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY
        order_ack.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
        order_ack.ExecType.value = Fix.Tags.ExecType.Values.NEW
        order_ack.LeavesQty.value = TRiskManager.qty
        order_ack.CumQty.value = TRiskManager.qty

        return order_ack

    @staticmethod
    def __create_order_cancel_request() -> Fix.Messages.OrderCancelRequest:
        """
        Create a new order single
        :return: New order single
        """
        order_cancel_request = Fix.Messages.OrderCancelRequest()
        side = Fix.Tags.Side.Values.BUY
        order_cancel_request.Instrument.Symbol.value = TRiskManager.instmt
        order_cancel_request.Instrument.SecurityExchange.value = TRiskManager.exchange_name
        order_cancel_request.Side.value = side
        order_cancel_request.ClOrdID.value = 'OrderCancelRequest%.6f' % TRiskManager.price

        return order_cancel_request

    def test_position_report(self):
        """
        Test position report
        """
        risk_manager = RiskManager()
        message = self.__create_position_report()
        exchange_risk = risk_manager.register_exchange(self.exchange_name)
        risk_manager.update_risk_exposure_by_message(message, exchange_risk)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').balance, 2000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').available_balance, 2000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').available_balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').balance, 1)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').available_balance, 1)

    def test_send_order(self):
        """
        Test send order
        """
        risk_manager = RiskManager()
        message = self.__create_position_report()
        exchange_risk = risk_manager.register_exchange(self.exchange_name)
        risk_manager.update_risk_exposure_by_message(message, exchange_risk)

        # Send order
        new_order_single = self.__create_new_order_single()
        risk_manager.update_risk_exposure_by_message(new_order_single, exchange_risk)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').balance, 2000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').available_balance, 2000 - self.price * self.qty)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').available_balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').balance, 1)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').available_balance, 1)

    def test_order_reject(self):
        """
        Test order reject
        :return:
        """
        risk_manager = RiskManager()
        message = self.__create_position_report()
        exchange_risk = risk_manager.register_exchange(self.exchange_name)
        risk_manager.update_risk_exposure_by_message(message, exchange_risk)

        # Send order
        new_order_single = self.__create_new_order_single()
        risk_manager.update_risk_exposure_by_message(new_order_single, exchange_risk)
        # Order reject
        order_reject = self.__create_order_reject()
        risk_manager.update_risk_exposure_by_message(order_reject, exchange_risk)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').balance, 2000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').available_balance, 2000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').available_balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').balance, 1)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').available_balance, 1)

    def test_order_ack(self):
        """
        Test order ack
        :return:
        """
        risk_manager = RiskManager()
        message = self.__create_position_report()
        exchange_risk = risk_manager.register_exchange(self.exchange_name)
        risk_manager.update_risk_exposure_by_message(message, exchange_risk)

        # Send order
        new_order_single = self.__create_new_order_single()
        risk_manager.update_risk_exposure_by_message(new_order_single, exchange_risk)
        # Order ack
        order_ack = self.__create_order_ack()
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').balance, 2000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').available_balance, 2000 - self.price * self.qty)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').available_balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').balance, 1)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').available_balance, 1)

    def test_order_execution(self):
        """
        Test order execution
        """
        risk_manager = RiskManager()
        message = self.__create_position_report()
        exchange_risk = risk_manager.register_exchange(self.exchange_name)
        risk_manager.update_risk_exposure_by_message(message, exchange_risk)

        # Send order
        new_order_single = self.__create_new_order_single()
        risk_manager.update_risk_exposure_by_message(new_order_single, exchange_risk)
        # Order ack
        order_ack = self.__create_order_ack()
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        # Order execution
        order_ack.ExecType.value = Fix.Tags.ExecType.Values.TRADE
        order_ack.LastPx.value = order_ack.Price.value
        order_ack.LastQty.value = order_ack.OrderQtyData.OrderQty.value * 0.25
        order_ack.CumQty.value = order_ack.LastQty.value
        order_ack.LeavesQty.value = order_ack.OrderQtyData.OrderQty.value * 0.75
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').balance, 2000 - (self.price * self.qty * 0.25))
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').available_balance, 2000 - self.price * self.qty)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').available_balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').balance, 1 + self.qty * 0.25)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').available_balance, 1 + self.qty * 0.25)

    def test_send_order_cancel_request(self):
        """
        Test send order cancel request
        :return:
        """
        risk_manager = RiskManager()
        message = self.__create_position_report()
        exchange_risk = risk_manager.register_exchange(self.exchange_name)
        risk_manager.update_risk_exposure_by_message(message, exchange_risk)

        # Send order
        new_order_single = self.__create_new_order_single()
        risk_manager.update_risk_exposure_by_message(new_order_single, exchange_risk)
        # Order ack
        order_ack = self.__create_order_ack()
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        # Order execution
        order_ack.ExecType.value = Fix.Tags.ExecType.Values.TRADE
        order_ack.LastPx.value = order_ack.Price.value
        order_ack.LastQty.value = order_ack.OrderQtyData.OrderQty.value * 0.25
        order_ack.CumQty.value = order_ack.LastQty.value
        order_ack.LeavesQty.value = order_ack.OrderQtyData.OrderQty.value * 0.75
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        # Send cancel
        order_cancel_request = self.__create_order_cancel_request()
        risk_manager.update_risk_exposure_by_message(order_cancel_request, exchange_risk)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').balance, 2000 - (self.price * self.qty * 0.25))
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').available_balance, 2000 - self.price * self.qty)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').available_balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').balance, 1 + self.qty * 0.25)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').available_balance, 1 + self.qty * 0.25)

    def test_send_cancel_ack(self):
        """
        Test send order cancel request
        :return:
        """
        risk_manager = RiskManager()
        message = self.__create_position_report()
        exchange_risk = risk_manager.register_exchange(self.exchange_name)
        risk_manager.update_risk_exposure_by_message(message, exchange_risk)

        # Send order
        new_order_single = self.__create_new_order_single()
        risk_manager.update_risk_exposure_by_message(new_order_single, exchange_risk)
        # Order ack
        order_ack = self.__create_order_ack()
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        # Order execution
        order_ack.ExecType.value = Fix.Tags.ExecType.Values.TRADE
        order_ack.LastPx.value = order_ack.Price.value
        order_ack.LastQty.value = order_ack.OrderQtyData.OrderQty.value * 0.25
        order_ack.CumQty.value = order_ack.LastQty.value
        order_ack.LeavesQty.value = order_ack.OrderQtyData.OrderQty.value * 0.75
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        # Send cancel
        order_cancel_request = self.__create_order_cancel_request()
        risk_manager.update_risk_exposure_by_message(order_cancel_request, exchange_risk)
        # Cancel ack
        order_ack.OrdStatus.value = Fix.Tags.OrdStatus.Values.CANCELED
        order_ack.ExecType.value = Fix.Tags.ExecType.Values.CANCELED
        order_ack.LeavesQty.value = 0
        risk_manager.update_risk_exposure_by_message(order_ack, exchange_risk)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').balance, 2000 - (self.price * self.qty * 0.25))
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'USD').available_balance, 2000 - (self.price * self.qty * 0.25))
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'HKD').available_balance, 10000)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').balance, 1 + self.qty * 0.25)
        self.assertEqual(risk_manager.get_exchange_balance(self.exchange_name, 'BTC').available_balance, 1 + self.qty * 0.25)
