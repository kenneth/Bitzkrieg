#!/bin/python
from bitz.order_server import OrderServer
from bitz.journal_database import InternalJournalDatabase
from bitz.realtime_database import InternalRealtimeDatabase
from bitz.risk_manager import RiskManager
from bitz.file_market_data_feed import FileMarketDataFeed
from bitz.exch_backtesting import ExchBacktesting
from bitz.logger import ConsoleLogger
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.instrument import Instrument, InstrumentList
from typing import Tuple
from uuid import uuid4 as uuid
import unittest
import os

class TOrderServer(unittest.TestCase):
    exchange_name = 'quoine'
    instmt = 'btcusd'

    def __initialize_order_server(self) -> Tuple[OrderServer, ExchBacktesting]:
        """
        Initialize order server
        :return: Order server and the backtesting exchange gateway
        """
        instrument_list = InstrumentList()
        instrument_list.insert(Instrument(exchange=TOrderServer.exchange_name,
                                          instmt_name=TOrderServer.instmt,
                                          usd_rate=1,
                                          price_min_size=0.01,
                                          qty_min_size=0.01,
                                          base_currency='USD',
                                          quote_currency='BTC'))
        journal_db = InternalJournalDatabase()
        realtime_db = InternalRealtimeDatabase()
        risk_manager = RiskManager(instrument_list)

        test_files = [os.path.join('bitz', 'test', 'exch_quoine_btcusd_snapshot_20170407.csv')]
        market_data_feed = FileMarketDataFeed(ConsoleLogger.static_logger)
        market_data_feed.connect(files=test_files)

        order_server = OrderServer(ConsoleLogger.static_logger,
                                   journal_db,
                                   realtime_db,
                                   risk_manager,
                                   market_data_feed,
                                   InstrumentList)

        # Register the gateway
        gw = ExchBacktesting(self.exchange_name, market_data_feed)
        order_server.register_exchange(gw)

        return order_server, gw

    def __create_new_order_single(self, order_server: OrderServer) -> Fix.Messages.NewOrderSingle:
        """
        Create a new order single
        :return: New order single
        """
        new_order_single = Fix.Messages.NewOrderSingle()
        snapshot = order_server.market_data_feed.get_exchange_snapshot(self.exchange_name, self.instmt)
        price = snapshot.order_book.b1
        qty = 1
        side = Fix.Tags.Side.Values.BUY
        new_order_single.Instrument.Symbol.value = snapshot.instmt
        new_order_single.Instrument.SecurityExchange.value = snapshot.exchange
        new_order_single.Price.value = price
        new_order_single.TriggeringInstruction.TriggerPrice.value = price
        new_order_single.Side.value = side
        new_order_single.ClOrdID.value = str(uuid())
        new_order_single.OrderQtyData.OrderQty.value = qty
        new_order_single.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        new_order_single.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY

        # Set triggering quantity. If the price is not with the first 5 price range,
        # set it as 0 for triggering quantity.
        new_order_single.TriggeringInstruction.TriggerPrice.value = price
        new_order_single.TriggeringInstruction.TriggerNewQty.value = 0
        if side == Fix.Tags.Side.Values.BUY:
            for tpx, tqty in [(snapshot.order_book.b1, snapshot.order_book.bq1),
                              (snapshot.order_book.b2, snapshot.order_book.bq2),
                              (snapshot.order_book.b3, snapshot.order_book.bq3),
                              (snapshot.order_book.b4, snapshot.order_book.bq4),
                              (snapshot.order_book.b5, snapshot.order_book.bq5)]:
                if tpx == new_order_single.TriggeringInstruction.TriggerPrice.value:
                    new_order_single.TriggeringInstruction.TriggerNewQty.value = tqty
                    break
        else:
            for tpx, tqty in [(snapshot.order_book.a1, snapshot.order_book.aq1),
                              (snapshot.order_book.a2, snapshot.order_book.aq2),
                              (snapshot.order_book.a3, snapshot.order_book.aq3),
                              (snapshot.order_book.a4, snapshot.order_book.aq4),
                              (snapshot.order_book.a5, snapshot.order_book.aq5)]:
                if tpx == new_order_single.TriggeringInstruction.TriggerPrice.value:
                    new_order_single.TriggeringInstruction.TriggerNewQty.value = tqty
                    break

        return new_order_single

    @classmethod
    def __create_order_cancel_request(cls, last_update: Fix.Messages.ExecutionReport) -> Fix.Messages.OrderCancelRequest:
        """
        Create order cancel request
        :param last_update: Last update
        :return: Order cancel request
        """
        order_cancel_request = Fix.Messages.OrderCancelRequest()
        order_cancel_request.ClOrdID.value = str(uuid())
        order_cancel_request.Instrument.Symbol.value = last_update.Instrument.Symbol.value
        order_cancel_request.Instrument.SecurityExchange.value = last_update.Instrument.SecurityExchange.value
        order_cancel_request.OrderID.value = last_update.OrderID.value
        order_cancel_request.Side.value = last_update.Side.value
        return order_cancel_request

    def test_register_gateway(self):
        """
        Test to register gateway twice
        """
        order_server, gateway = self.__initialize_order_server()

        # Register the gateway again
        with self.assertRaises(AssertionError) as context:
            order_server.register_exchange(gateway)

        self.assertTrue(("Exchange %s is duplicated." % self.exchange_name.upper()) in str(context.exception))

    def test_initialize_exchange_risk(self):
        """
        Test to initialize exchange risk
        """
        order_server, gateway = self.__initialize_order_server()
        order_server.initialize_exchange_risk()
        # Upper string
        hkd_risk = order_server.risk_manager.get_exchange_balance(self.exchange_name, 'HKD')
        self.assertEqual(hkd_risk.balance, 100000)
        self.assertEqual(hkd_risk.available_balance, 100000)
        # Lower string
        hkd_risk = order_server.risk_manager.get_exchange_balance(self.exchange_name, 'hkd')
        self.assertEqual(hkd_risk.balance, 100000)
        self.assertEqual(hkd_risk.available_balance, 100000)

    def test_place_order(self):
        """
        Test to place an order
        :return:
        """
        order_server, gateway = self.__initialize_order_server()
        order_server.initialize_exchange_risk()

        # Send the new order single request
        new_order_single = self.__create_new_order_single(order_server)
        responses, err_msg = order_server.request(new_order_single)

        # Check the result
        self.assertEqual(len(responses), 1)
        response = responses[0]
        # Assert risk
        hkd_risk = order_server.risk_manager.get_exchange_balance(self.exchange_name, 'USD')
        self.assertEqual(hkd_risk.balance, 2000)
        self.assertEqual(hkd_risk.available_balance, 2000 - new_order_single.Price.value * new_order_single.OrderQtyData.OrderQty.value)
        # Assert response
        self.assertEqual(response.MsgType, Fix.Tags.MsgType.Values.EXECUTIONREPORT)
        self.assertEqual(response.Instrument.Symbol.value, new_order_single.Instrument.Symbol.value)
        self.assertEqual(response.Instrument.SecurityExchange.value, new_order_single.Instrument.SecurityExchange.value)
        self.assertEqual(response.OrdStatus.value, Fix.Tags.OrdStatus.Values.NEW)
        self.assertEqual(response.ExecType.value, Fix.Tags.ExecType.Values.NEW)
        self.assertEqual(response.Price.value, new_order_single.Price.value)
        self.assertEqual(response.OrderQtyData.OrderQty.value, new_order_single.OrderQtyData.OrderQty.value)
        self.assertEqual(response.ClOrdID.value, new_order_single.ClOrdID.value)
        self.assertEqual(response.LeavesQty.value, new_order_single.OrderQtyData.OrderQty.value)
        self.assertEqual(response.CumQty.value, 0)

    def test_cancel_order(self):
        """
        Test to cancel an order
        :return:
        """
        order_server, gateway = self.__initialize_order_server()
        order_server.initialize_exchange_risk()

        # Send the new order single request
        new_order_single = self.__create_new_order_single(order_server)
        responses, err_msg = order_server.request(new_order_single)

        # Send the order cancel request
        order_cancel_request = self.__create_order_cancel_request(responses[0])
        responses, err_msg = order_server.request(order_cancel_request)

        # Check the result
        self.assertEqual(len(responses), 1)
        response = responses[0]
        # Assert risk
        hkd_risk = order_server.risk_manager.get_exchange_balance(self.exchange_name, 'USD')
        self.assertEqual(hkd_risk.balance, 2000)
        self.assertEqual(hkd_risk.available_balance, 2000)
        # Assert response
        self.assertEqual(response.MsgType, Fix.Tags.MsgType.Values.EXECUTIONREPORT)
        self.assertEqual(response.Instrument.Symbol.value, new_order_single.Instrument.Symbol.value)
        self.assertEqual(response.Instrument.SecurityExchange.value, new_order_single.Instrument.SecurityExchange.value)
        self.assertEqual(response.OrdStatus.value, Fix.Tags.OrdStatus.Values.CANCELED)
        self.assertEqual(response.ExecType.value, Fix.Tags.ExecType.Values.CANCELED)
        self.assertEqual(response.Price.value, new_order_single.Price.value)
        self.assertEqual(response.OrderQtyData.OrderQty.value, new_order_single.OrderQtyData.OrderQty.value)
        self.assertEqual(response.ClOrdID.value, order_cancel_request.ClOrdID.value)
        self.assertEqual(response.CumQty.value, 0)
        self.assertEqual(response.LeavesQty.value, 0)
        self.assertEqual(response.CumQty.value, 0)

    def test_cancel_order_reject(self):
        """
        Test to cancel an order
        :return:
        """
        order_server, gateway = self.__initialize_order_server()
        order_server.initialize_exchange_risk()

        # Send the new order single request
        new_order_single = self.__create_new_order_single(order_server)
        responses, err_msg = order_server.request(new_order_single)

        # Send the order cancel request
        order_cancel_request = self.__create_order_cancel_request(responses[0])
        responses, err_msg = order_server.request(order_cancel_request)

        # Send the order cancel request again. Expects rejected.
        order_cancel_request = self.__create_order_cancel_request(responses[0])
        responses, err_msg = order_server.request(order_cancel_request)

        # Check the result
        self.assertEqual(len(responses), 1)
        response = responses[0]
        # Assert risk
        hkd_risk = order_server.risk_manager.get_exchange_balance(self.exchange_name, 'USD')
        self.assertEqual(hkd_risk.balance, 2000)
        self.assertEqual(hkd_risk.available_balance, 2000)
        # Assert response
        self.assertEqual(response.MsgType, Fix.Tags.MsgType.Values.ORDERCANCELREJECT)
        self.assertEqual(response.ClOrdID.value, order_cancel_request.ClOrdID.value)





