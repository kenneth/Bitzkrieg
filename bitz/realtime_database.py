#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix
from typing import Union

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
        # Execution report cache. (OrderID, Exchange, Instmt) is the key, while the latest execution report
        # is the value
        self.__historical_requests = {}
        self.__execution_report_cache = {}

    def connect(self, **kwargs):
        """
        Connect to the database
        :param kwargs: Arguments
        """
        pass

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


