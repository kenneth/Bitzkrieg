#!/bin/python
from bitz.FIX50SP2 import FIX50SP2 as Fix
from datetime import datetime

class FixMessageFactory(object):
    """
    FIX message factory
    """
    @classmethod
    def create_new_single_order(cls,
                                symbol=None,
                                exchange=None,
                                clordid=None,
                                price=None,
                                qty=None,
                                side=Fix.Tags.Side.Values.BUY,
                                ordtype=Fix.Tags.OrdType.Values.LIMIT,
                                timeinforce=Fix.Tags.TimeInForce.Values.DAY,
                                transacttime=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f")):
        """
        Create a NewSingleOrder
        """
        assert  symbol is not None and \
                exchange is not None and \
                clordid is not None and \
                price is not None and \
                qty is not None, "Empty mandatory field(s)."
        new_order_single = Fix.Messages.NewOrderSingle()
        new_order_single.Instrument.Symbol.value = symbol
        new_order_single.Instrument.SecurityExchange.value = exchange
        new_order_single.ClOrdID.value = clordid
        new_order_single.Price.value = price
        new_order_single.TriggeringInstruction.TriggerPrice.value = price
        new_order_single.Side.value = side
        new_order_single.ClOrdID.value = clordid
        new_order_single.OrderQtyData.OrderQty.value = qty
        new_order_single.OrdType.value = ordtype
        new_order_single.TimeInForce.value = timeinforce
        new_order_single.TransactTime.value = transacttime
        return new_order_single

    @classmethod
    def create_execution_report(cls,
                                symbol=None,
                                exchange=None,
                                clordid=None,
                                orderid=None,
                                price=None,
                                qty=None,
                                side=Fix.Tags.Side.Values.BUY,
                                ordtype=Fix.Tags.OrdType.Values.LIMIT,
                                timeinforce=Fix.Tags.TimeInForce.Values.DAY,
                                transacttime=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                ordstatus=Fix.Tags.OrdStatus.Values.NEW,
                                exectype=Fix.Tags.ExecType.Values.NEW,
                                origclordid=None,
                                leavesqty=0,
                                cumqty=0,
                                lastpx=None,
                                lastqty=None,
                                avgpx=None):
        assert  symbol is not None and \
                exchange is not None and \
                clordid is not None and \
                orderid is not None and \
                price is not None and \
                qty is not None, "Empty mandatory field(s)."
        execution_report = Fix.Messages.ExecutionReport()
        execution_report.Instrument.Symbol.value = symbol
        execution_report.Instrument.SecurityExchange.value = exchange
        execution_report.OrderID.value = orderid
        execution_report.ClOrdID.value = clordid
        if origclordid is not None:
            execution_report.OrigClOrdID.value = origclordid
        execution_report.Price.value = price
        execution_report.OrderQtyData.value = qty
        execution_report.Side.value = side
        execution_report.OrdType.value = ordtype
        execution_report.TimeInForce.value = timeinforce
        execution_report.TransactTime.value = transacttime
        execution_report.OrdStatus.value = ordstatus
        execution_report.ExecType.value = exectype
        execution_report.LeavesQty.value = leavesqty
        if cumqty is not None:
            execution_report.CumQty.value = cumqty
        if lastpx is not None:
            execution_report.LastPx.value = lastpx
        if lastqty is not None:
            execution_report.LastQty.value = lastqty
        if avgpx is not None:
            execution_report.AvgPx.value = avgpx
        return execution_report

    @classmethod
    def create_execution_report_from_new_order_single(cls, req: Fix.Messages.NewOrderSingle, orderid):
        return cls.create_execution_report(symbol=req.Instrument.Symbol.value,
                                           exchange=req.Instrument.SecurityExchange.value,
                                           orderid=orderid,
                                           clordid=req.ClOrdID.value,
                                           price=req.Price.value,
                                           qty=req.OrderQtyData.OrderQty.value,
                                           side=req.Side.value,
                                           ordtype=req.OrdType.value,
                                           timeinforce=req.TimeInForce.value,
                                           transacttime=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                           ordstatus=Fix.Tags.OrdStatus.Values.NEW,
                                           exectype=Fix.Tags.ExecType.Values.NEW,
                                           leavesqty=req.OrderQtyData.OrderQty.value,
                                           cumqty=0)



