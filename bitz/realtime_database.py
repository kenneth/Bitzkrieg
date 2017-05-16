#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix
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
        pass

    def connect(self, **kwargs):
        """
        Connect to the database
        :param kwargs: Arguments
        """
        raise NotImplementedError("Not yet implemented")

    def update(self, request, exe_report: Fix.Messages.ExecutionReport):
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
        # Historial requests. (OrderID, Exchange, Instmt) is the key, while the request is the value
        self.__historical_requests = {}
        # Execution report cache. (OrderID, Exchange, Instmt) is the key, while the latest execution report
        # is the value
        self.__execution_report_cache = {}

    def __del__(self):
        """
        Destructor
        """
        if self.__output_path != '':
            file = open(os.path.join(self.__output_path, 'historical_requests_%s.db' % datetime.utcnow().strftime('%Y%m%d%H%M%S')),
                        'w+')
            for key in sorted(self.__historical_requests.keys()):
                file.write('\'%s\',%s\n' % (key, fixmsg2dict(self.__historical_requests[key][-1])))
            file.close()

            file = open(os.path.join(self.__output_path, 'execution_report_cache_%s.db' % datetime.utcnow().strftime('%Y%m%d%H%M%S')),
                        'w+')
            for key in sorted(self.__execution_report_cache.keys()):
                file.write('\'%s\',%s\n' % (key, fixmsg2dict(self.__execution_report_cache[key][-1])))
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

    def update(self, request, response: Union[Fix.Messages.ExecutionReport, Fix.Messages.OrderCancelReject]):
        """
        Update the latest order information
        :param response: Execution report
        """
        order_id = response.OrderID.value
        if order_id is not None:
            exchange = response.Instrument.SecurityExchange.value
            instmt = response.Instrument.Symbol.value
            key = (order_id, exchange, instmt)
            self.__execution_report_cache.setdefault(key, []).append(response)
            self.__historical_requests.setdefault(key, []).append(request)
        else:
            if response.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
                assert response.ExecType.value == Fix.Tags.ExecType.Values.REJECTED, \
                        "ExecType(%s) is not rejected at ER (%s)" % (response.ExecType.value, response.ExecID.value)

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
            if key in self.__execution_report_cache.keys():
                return self.__execution_report_cache[key][-1]
            else:
                return None
        else:
            return None


