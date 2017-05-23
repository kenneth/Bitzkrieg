#!/usr/bin/python3
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.logger import Logger
from bitz.journal_database import AbstractJournalDatabase
from bitz.realtime_database import AbstractRealtimeDatabase
from bitz.risk_manager import RiskManager
from bitz.market_data_feed import MarketDataFeed
from bitz.util import update_fixtime, fixmsg2dict
from bitz.market_data import Snapshot
from datetime import datetime
from typing import Union, List, Tuple
from uuid import uuid4 as uuid


class OrderServer:
    """
    Order server

    The server contains the following components:
    1. Journal database connection
    2. Order snapshot data connection
    3. Market data feed
    4. RIsk manager

    Order identifier:
    Symbol + SecurityExchange + OrderID

    All the communication is via FIX protocol.
    """
    class Mode:
        PROD = 0
        SIM = 1

    def __init__(self,
                 logger: Logger,
                 journal_db: AbstractJournalDatabase,
                 realtime_db: AbstractRealtimeDatabase,
                 risk_manager: RiskManager,
                 market_data_feed: MarketDataFeed):
        """
        Constructor
        """
        self.logger = logger
        self.journal_db = journal_db
        self.realtime_db = realtime_db
        self.risk_manager = risk_manager
        self.exchanges = {}
        self.current_exec_id = 0
        self.market_data_feed = market_data_feed

    def __del__(self):
        """
        Destructor
        """
        if self.market_data_feed is not None:
            self.market_data_feed.disconnect()

    def now(self):
        """
        Get the server current time.
        :return: Current datetime in GMT.
        """
        return self.market_data_feed.now()

    def now_string(self, format='%Y%m%dT%H:%M:%S.%f'):
        """
        Get the server current time in string
        :return: Current datetime in string.
        """
        return self.market_data_feed.now_string(format)

    def get_latest_snapshot(self, timeout=100) -> Snapshot:
        """
        Get market data feed snapshot
        """
        snapshot = self.market_data_feed.get_snapshot(timeout)
        if isinstance(snapshot, Snapshot):
            for exch_name, exch in self.exchanges.items():
                exch.snapshot_updated(snapshot)
        return snapshot

    def get_exchange_snapshot(self, exchange, instmt_name) -> Snapshot:
        """
        Get exchange snapshot
        :param exchange: Exchange name
        :param instmt_name: Instrument name
        :return The exchange snapshot. None if not found.
        """
        return self.market_data_feed.get_exchange_snapshot(exchange, instmt_name)

    def request(self, req) -> Tuple[List[object],str]:
        """
        Request
        1. Check if the exchange is registered
        2. Store the request into the journal db
        3. If the message type is
            a) NewOrderSingle - Add the risk exposure
            b) OrderCancelRequest and OrderCancelReplaceRequest - Check if the order is valid
            c) PositionRequest - No checking
        4. Route the request
        5. Store the response into the journal db
        6. Return the responses
        :param req: Request message
        :return: Responses
        """

        # Get the exchange
        exchange = self.__is_valid_exchange(req)

        # Log the request into the journal
        ok = self.__log_journal(req)
        assert ok, "Cannot log message into the journal database.\n%s" % req

        # Handle outgoing message
        self.__handle_outgoing_message(req)

        # Route the request to the exchange
        responses, err = exchange.request(req)

        # Handle incoming message
        for response in responses:
            self.__handle_incoming_message(response, req)
            # Log the response into the database
            ok &= self.__log_journal(response)
            assert ok, "Cannot log message into the journal database.\n%s" % response

        return responses, err

    def register_exchange(self, exchange):
        """
        Register exchange
        :param exchange; Exchange
        """
        name = exchange.get_name().upper()
        assert name not in self.exchanges.keys(), "Exchange %s is duplicated." % name
        self.exchanges[name] = exchange
        self.risk_manager.register_exchange(name)

    def initialize_exchange_risk(self):
        """
        Initialize exchange risk. This method is called when all the gateways are registered.
        """
        for exchange_name, exchange in self.exchanges.items():
            req = Fix.Messages.RequestForPositions()
            req.PosReqID.value = self.now_string() + str(uuid())
            req.Instrument.SecurityExchange.value = exchange_name
            update_fixtime(req, Fix.Tags.TransactTime.Tag, self.now_string())
            responses, err_msg = self.request(req)
            assert err_msg == "", "Error (%s) is found." % err_msg
            assert len(responses) == 1, "Expect to have only one response."

    def valid_risk_limit(self, message: Fix.Messages.NewOrderSingle):
        """
        Valid the risk limit
        :param message: New order single
        :return: True if pass.
        """
        return self.risk_manager.risk_check(message)

    def __is_valid_exchange(self, message):
        """
        Check if it is a valid exchange
        :param message: Message
        :return The exchange gateway if it is valid
        """
        exchange = message.Instrument.SecurityExchange.value.upper()
        assert exchange in self.exchanges.keys(), "Cannot find exchange %s" % exchange
        return self.exchanges[exchange]

    def __log_journal(self, message):
        """
        Log the message into the journal database
        :param message: Message
        """
        key = ''
        msgType = message.MsgType
        if msgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE or \
            msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST or \
            msgType == Fix.Tags.MsgType.Values.ORDERCANCELREPLACEREQUEST:
            key = message.ClOrdID.value
        elif msgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
            if message.ExecID.value is None:
                message.ExecID.value = '%s%s' % (self.now_string(), uuid())
            key = message.ExecID.value
        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREJECT:
            key = message.ClOrdID.value + self.now_string()
        elif msgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            key = message.PosReqID.value
        elif msgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST:
            key = message.OrdStatusReqID.value
        elif msgType == Fix.Tags.MsgType.Values.POSITIONREPORT:
            key = message.PosMaintRptID.value
        else:
            raise NotImplementedError("MsgType (%s) has not yet been implemented." % msgType)

        assert key is not None, "MsgType (%s) has an empty key.\n%s" % (msgType, fixmsg2dict(message))

        return self.journal_db.insert(key, fixmsg2dict(message))

    def __check_active_order(self, message):
        """
        Check if the order is active in the book
        :param message: Message
        :return: True if it is active
        """
        if message.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREPLACEREQUEST or \
            message.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            return self.realtime_db.get_latest_by_order_id(message) is not None
        else:
            raise NotImplementedError("Message type %s has not yet been implemented" % message.MsgType)

    def __handle_outgoing_message(self, message):
        """
        Handle outgoing messages.
        :param message: Message
        """
        msgType = message.MsgType

        # Update risk exposure
        exchange = message.Instrument.SecurityExchange.value
        exchange_risk = self.risk_manager.get_exchange_balance(exchange)
        RiskManager.update_risk_exposure_by_message(message, exchange_risk)

        # Check the message type
        if msgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            pass
        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREPLACEREQUEST:
            ok = self.__check_active_order(message)
        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            ok = self.__check_active_order(message)
        elif msgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            pass
        elif msgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            pass
        elif msgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST:
            pass
        else:
            raise NotImplementedError("Message type %s has not yet been implemented" % message.MsgType)

    def __handle_incoming_message(self, message, request=None):
        """
        Handle incoming message
        :param message: Incoming message
        :param request: Original request
        :return:
        """
        msgType = message.MsgType

        # Check the message type
        if msgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
            if message.OrdStatus.value in [Fix.Tags.OrdStatus.Values.CANCELED,
                                           Fix.Tags.OrdStatus.Values.FILLED,
                                           Fix.Tags.OrdStatus.Values.PARTIALLY_FILLED]:
                self.__supply_information_if_missing(request, message)
            self.__supply_transacttime_if_missing(message)
            self.realtime_db.update_order(request, message)
        elif msgType == Fix.Tags.MsgType.Values.POSITIONREPORT:
            self.realtime_db.update_balances(request, message)
        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREJECT:
            self.__supply_transacttime_if_missing(message)
        else:
            raise NotImplementedError("Message type %s has not yet been implemented" % message.MsgType)

        # Update risk exposure
        if msgType not in [Fix.Tags.MsgType.Values.ORDERCANCELREJECT]:
            exchange = message.Instrument.SecurityExchange.value
            exchange_risk = self.risk_manager.get_exchange_balance(exchange)
            RiskManager.update_risk_exposure_by_message(message, exchange_risk)

    def __supply_information_if_missing(self, req, message: Fix.Messages.ExecutionReport):
        """
        Supply the order information, e.g. orderqty and cumqty, if missing
        :param message: Message
        """
        latest_status = self.realtime_db.get_latest_by_order_id(req)
        if latest_status is not None:
            if message.Side.value is None:
                message.Side.value = latest_status.Side.value
            if message.Price.value is None:
                message.Price.value = latest_status.Price.value
            if message.OrderQtyData.OrderQty.value is None:
                message.OrderQtyData.OrderQty.value = latest_status.OrderQtyData.OrderQty.value
            if message.CumQty.value is None:
                message.CumQty.value = latest_status.CumQty.value
            if message.AvgPx.value is None:
                message.AvgPx.value = latest_status.AvgPx.value
            if message.LeavesQty.value is None:
                message.LeavesQty.value = latest_status.LeavesQty.value

    def __supply_transacttime_if_missing(self, message):
        """
        Supply the tag 60 if missing
        :param message: Message
        """
        if message.TransactTime.value is None:
            message.TransactTime.value = self.now_string()


