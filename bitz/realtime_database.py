#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.sql_client import SqliteClient, MysqliteClient
from bitz.db_records import ActiveOrders, Balances, OrderRequests
from bitz.util import fixmsg2dict
from typing import Union
from datetime import datetime
import os

class AbstractRealtimeDatabase(object):
    """
    Abstract realtime database
    """
    def __init__(self):
        """
        Constructor
        """
        # Historial requests. (OrderID, Exchange, Instmt) is the key, while the request is the value
        self._historical_requests = {}
        # Execution report cache. (OrderID, Exchange, Instmt) is the key, while the latest execution report
        # is the value
        self._execution_report_cache = {}
        # Position report cache. (Exchange) is the key, while the request is the latest position report
        # Assuming the position report covers all currency
        self._position_report_cache = {}

    def connect(self, **kwargs):
        """
        Connect to the database
        :param kwargs: Arguments
        """
        raise NotImplementedError("Not yet implemented")

    def update_order(self, request, exe_report: Fix.Messages.ExecutionReport):
        """
        Update the latest order information
        :param exe_report: Execution report
        """
        raise NotImplementedError("Not yet implemented")

    def update_balances(self, request, pos_report: Fix.Messages.PositionReport):
        """
        Update the latest order information
        :param exe_report: Execution report
        """
        raise NotImplementedError("Not yet implemented")

    def get_latest_by_order_id(self, request):
        """
        Get the latest execution report by order id
        :param request: Request
        :return: Latest execution report. None if not found
        """
        raise NotImplementedError("Not yet implemented")

class InternalRealtimeDatabase(AbstractRealtimeDatabase):
    """
    Internal memory realtime database
    """
    def __init__(self):
        """
        Constructor
        """
        AbstractRealtimeDatabase.__init__(self)
        self.__output_path = ''

    def __del__(self):
        """
        Destructor
        """
        if self.__output_path != '':
            file = open(os.path.join(self.__output_path, 'historical_requests_%s.db' % datetime.utcnow().strftime('%Y%m%d%H%M%S')),
                        'w+')
            for key in sorted(self._historical_requests.keys()):
                file.write('\'%s\',%s\n' % (key, fixmsg2dict(self._historical_requests[key][-1])))
            file.close()

            file = open(os.path.join(self.__output_path, 'execution_report_cache_%s.db' % datetime.utcnow().strftime('%Y%m%d%H%M%S')),
                        'w+')
            for key in sorted(self._execution_report_cache.keys()):
                file.write('\'%s\',%s\n' % (key, fixmsg2dict(self._execution_report_cache[key][-1])))
            file.close()

            file = open(os.path.join(self.__output_path, 'position_report_cache_%s.db' % datetime.utcnow().strftime('%Y%m%d%H%M%S')),
                        'w+')
            for key in sorted(self._position_report_cache.keys()):
                file.write('\'%s\',%s\n' % (key, fixmsg2dict(self._position_report_cache[key][-1])))
            file.close()

    def connect(self, **kwargs):
        """
        Connect to the database
        :param kwargs: Arguments
        """
        self.__output_path = kwargs.setdefault('path', '')
        if not os.path.isdir(self.__output_path):
            prev_path = self.__output_path
            self.__output_path = ''
            assert False, "Invalid output path (%s)" % prev_path

    def update_order(self, request, response: Union[Fix.Messages.ExecutionReport, Fix.Messages.OrderCancelReject]):
        """
        Update the latest order information
        :param response: Execution report
        """
        order_id = response.OrderID.value
        if order_id is not None:
            exchange = response.Instrument.SecurityExchange.value
            instmt = response.Instrument.Symbol.value
            key = (order_id, exchange, instmt)
            self._execution_report_cache.setdefault(key, []).append(response)
            self._historical_requests.setdefault(key, []).append(request)
        else:
            if response.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
                assert response.ExecType.value == Fix.Tags.ExecType.Values.REJECTED, \
                        "ExecType(%s) is not rejected at ER (%s)" % (response.ExecType.value, response.ExecID.value)

    def update_balances(self, request, pos_report: Fix.Messages.PositionReport):
        """
        Update the latest balances  information
        :param pos_report: Position report
        """
        if pos_report.MsgType != Fix.Tags.MsgType.Values.POSITIONREPORT:
            NotImplementedError("Unknown Fix Message Type")
        self._position_report_cache.setdefault(pos_report.Instrument.SecurityExchange.value, []).append(pos_report)

    def get_latest_by_order_id(self, request):
        """
        Get the latest execution report by order id
        :param request: Request
        :return: Latest execution report. None if not found
        """
        order_id = request.OrderID.value
        if order_id is not None:
            exchange = request.Instrument.SecurityExchange.value
            instmt = request.Instrument.Symbol.value
            key = (order_id, exchange, instmt)
            if key in self._execution_report_cache.keys():
                return self._execution_report_cache[key][-1]
            else:
                return None
        else:
            return None


class SqlRealtimeDatabase(InternalRealtimeDatabase):
    """
    Abstract realtime database
    """
    class DatabaseType:
        """
        Database type enum
        """
        UNKNOWN = 0
        SQLITE = 1
        MYSQL = 2

    def __init__(self, type=DatabaseType.UNKNOWN):
        """
        Constructor
        """
        InternalRealtimeDatabase.__init__(self)
        self.__client = None
        self.__type = type
        assert self.__type != SqlRealtimeDatabase.DatabaseType.UNKNOWN, \
                "Invalid SQL database type (%s)" % self.__type

    def __del__(self):
        """
        Destructor
        """
        # Do nothing
        pass

    def connect(self, **kwargs):
        """
        Connect to the database
        :param kwargs: Arguments
        """
        if self.__type == SqlRealtimeDatabase.DatabaseType.SQLITE:
            self.__client = SqliteClient()
            path = kwargs['path']
            self.__client.connect(path=path)
        elif self.__type == SqlRealtimeDatabase.DatabaseType.MYSQL:
            self.__client = MysqliteClient()
            host = kwargs['host']
            port = int(kwargs['port'])
            user = kwargs['user']
            pwd = kwargs['pwd']
            schema = kwargs['schema']
            self.__client.connect(host=host, port=port, user=user, pwd=pwd, schema=schema)
        else:
            raise NotImplementedError("SQL database type (%s) has not been implemented" % self.__type)

        self.__client.create(ActiveOrders)
        self.__client.create(Balances)
        self.__client.create(OrderRequests)

    def update_order(self, request, report: Fix.Messages.ExecutionReport):
        """
        Update the latest order information
        :param exe_report: Execution report
        """
        InternalRealtimeDatabase.update_order(self, request, report)

        # Update order requests
        if request.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            order_request = OrderRequests(timestamp=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                          msgtype=request.MsgType,
                                          exchange=request.Instrument.SecurityExchange.value,
                                          instmt_name=request.Instrument.Symbol.value,
                                          clordid=request.ClOrdID.value,
                                          side=request.Side.value,
                                          price=request.Price.value,
                                          orderqty=request.OrderQtyData.OrderQty.value,
                                          ordtype=request.OrdType.value,
                                          timeinforce=request.TimeInForce.value,
                                          sendingtime=request.Header.SendingTime.value)
        elif request.MsgType ==  Fix.Tags.MsgType.Values.ORDERCANCELREPLACEREQUEST:
            order_request = OrderRequests(timestamp=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                          msgtype=request.MsgType,
                                          exchange=request.Instrument.SecurityExchange.value,
                                          instmt_name=request.Instrument.Symbol.value,
                                          clordid=request.ClOrdID.value,
                                          orderid=request.OrderID.value,
                                          side=request.Side.value,
                                          price=request.Price.value,
                                          orderqty=request.OrderQtyData.OrderQty.value,
                                          ordtype=request.OrdType.value,
                                          timeinforce=request.TimeInForce.value,
                                          sendingtime=request.Header.SendingTime.value)
        elif request.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            order_request = OrderRequests(timestamp=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                          msgtype=request.MsgType,
                                          exchange=request.Instrument.SecurityExchange.value,
                                          instmt_name=request.Instrument.Symbol.value,
                                          clordid=request.ClOrdID.value,
                                          orderid=request.OrderID.value,
                                          side=request.Side.value,
                                          sendingtime=request.Header.SendingTime.value)
        elif request.MsgType == Fix.Tags.MsgType.Values.ORDERSTATUSREQUEST:
            order_request = OrderRequests(timestamp=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                          msgtype=request.MsgType,
                                          exchange=request.Instrument.SecurityExchange.value,
                                          instmt_name=request.Instrument.Symbol.value,
                                          clordid=request.OrdStatusReqID.value,
                                          orderid=request.OrderID.value,
                                          sendingtime=request.Header.SendingTime.value)
        elif request.MsgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            order_request = OrderRequests(timestamp=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                          msgtype=request.MsgType,
                                          exchange=request.Instrument.SecurityExchange.value,
                                          instmt_name=request.Instrument.Symbol.value,
                                          clordid=request.MassStatusReqID.value,
                                          sendingtime=request.Header.SendingTime.value)
        else:
            assert False, "MsgType (%s) not yet implemented." % request.MsgType

        self.__client.insert(order_request)

        # Update active orders
        active_order = ActiveOrders(timestamp=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                    exchange=report.Instrument.SecurityExchange.value,
                                    instmt_name=report.Instrument.Symbol.value,
                                    orderid=report.OrderID.value,
                                    side=report.Side.value,
                                    price=report.Price.value,
                                    orderqty=report.OrderQtyData.OrderQty.value,
                                    cumqty=report.CumQty.value,
                                    leavesqty=report.LeavesQty.value,
                                    avgpx=report.AvgPx.value,
                                    ordstatus=report.OrdStatus.value,
                                    exectype=report.ExecType.value,
                                    ordtype=report.OrdType.value,
                                    timeinforce=report.TimeInForce.value,
                                    clordid=report.ClOrdID.value,
                                    transacttime=report.TransactTime.value)

        self.__client.insert(active_order)

    def update_balances(self, request, pos_report: Fix.Messages.PositionReport):
        """
        Update the latest balances  information
        :param pos_report: Position report
        """
        if pos_report.MsgType != Fix.Tags.MsgType.Values.POSITIONREPORT:
            NotImplementedError("Unknown Fix Message Type")

        InternalRealtimeDatabase.update_balances(self, request, pos_report)

        balances = {}
        available_balances = {}

        for position in pos_report.PositionAmountData.groups:
            currency = position.PositionCurrency.value.upper()
            value = position.PosAmt.value
            type = position.PosAmtType.value

            if type == Fix.Tags.PosAmtType.Values.CASH_AMOUNT:
                balances[currency] = value
            elif type == Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT:
                available_balances[currency] = value
            else:
                assert False, "Invalid position amount type %d" % type

        for currency in available_balances.keys():
            if currency not in balances.keys():
                raise NotImplementedError("Currency %s has available balances but no balances" % currency)

        for currency in balances.keys():
            ccyBalance = Balances(timestamp=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                  exchange=pos_report.Instrument.SecurityExchange.value,
                                  ccy=currency,
                                  balance=balances[currency],
                                  availableBalance=available_balances.get(currency, float('nan')))
            self.__client.insert(ccyBalance)

    def get_database(self):
        """
        Get the database
        :return:
        """
        return self.__client


