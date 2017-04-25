#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix

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

    def update(self, request, exe_report: Fix.Messages.ExecutionReport):
        """
        Update the latest order information
        :param exe_report: Execution report
        """
        order_id = exe_report.OrderID.value
        if order_id is not None:
            exchange = exe_report.Instrument.SecurityExchange.value
            instmt = exe_report.Instrument.Symbol.value
            key = (order_id, exchange, instmt)
            self.__execution_report_cache[key] = exe_report
            self.__historical_requests.setdefault(key, []).append(request)
        else:
            assert exe_report.ExecType.value == Fix.Tags.ExecType.Values.REJECTED, \
                    "ExecType(%s) is not rejected at ER (%s)" % (exe_report.ExecType.value, exe_report.ExecID.value)

