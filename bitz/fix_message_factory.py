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
                                leavesqty=None,
                                cumqty=None,
                                lastpx=None,
                                lastqty=None,
                                avgpx=None,
                                text=None):
        assert  symbol is not None and \
                exchange is not None and \
                clordid is not None and \
                orderid is not None, "Empty mandatory field(s)."
        execution_report = Fix.Messages.ExecutionReport()
        execution_report.Instrument.Symbol.value = symbol
        execution_report.Instrument.SecurityExchange.value = exchange
        execution_report.OrderID.value = orderid
        execution_report.ClOrdID.value = clordid
        execution_report.OrigClOrdID.value = origclordid
        execution_report.Price.value = price
        execution_report.OrderQtyData.OrderQty.value = qty
        execution_report.Side.value = side
        execution_report.OrdType.value = ordtype
        execution_report.TimeInForce.value = timeinforce
        execution_report.TransactTime.value = transacttime
        execution_report.OrdStatus.value = ordstatus
        execution_report.ExecType.value = exectype
        execution_report.LeavesQty.value = leavesqty
        execution_report.CumQty.value = cumqty
        execution_report.LastPx.value = lastpx
        execution_report.LastQty.value = lastqty
        execution_report.AvgPx.value = avgpx
        execution_report.Text.value = text
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

    @classmethod
    def create_execution_report_reject_from_new_order_single(cls,
                                                             req: Fix.Messages.NewOrderSingle,
                                                             rejecterrReason: Fix.Tags.OrdRejReason.Values,
                                                             rejecterrText):
        report = cls.create_execution_report(symbol=req.Instrument.Symbol.value,
                                           exchange=req.Instrument.SecurityExchange.value,
                                           clordid=req.ClOrdID.value,
                                           transacttime=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"),
                                           ordstatus=Fix.Tags.OrdStatus.Values.REJECTED,
                                           exectype=Fix.Tags.ExecType.Values.REJECTED)
        report.OrdRejReason.value = rejecterrReason
        report.Text.value = rejecterrText
        return report

    @classmethod
    def create_order_status_request(cls,
                                    symbol,
                                    exchange,
                                    orderid,
                                    reqId):
        request = Fix.Messages.OrderStatusRequest()
        request.Instrument.Symbol.value = symbol
        request.Instrument.SecurityExchange.value = exchange
        request.OrderID.value = orderid
        request.OrdStatusReqID.value = reqId
        return request

    @classmethod
    def create_order_mass_cancel_request(cls,
                                         clordid):
        request = Fix.Messages.OrderMassCancelRequest()
        request.ClOrdID.value = clordid
        request.MassCancelRequestType.value = Fix.Tags.MassCancelRequestType.Values.CANCEL_ALL_ORDERS
        return request

    @classmethod
    def create_order_mass_cancel_report(cls,
                                        req: Fix.Messages.OrderMassCancelReport,
                                        cancel_response=Fix.Tags.MassCancelResponse.Values.CANCEL_ALL_ORDERS):
        report = Fix.Messages.OrderMassCancelReport()
        report.ClOrdID.value = req.ClOrdID.value
        report.MassCancelRequestType.value = req.MassCancelRequestType.value
        report.MassCancelResponse.value = cancel_response
        return report

    @classmethod
    def create_order_cancel_request(cls,
                                    exchange,
                                    symbol,
                                    orderid,
                                    clordid):
        request = Fix.Messages.OrderCancelRequest()
        request.Instrument.SecurityExchange.value = exchange
        request.Instrument.Symbol.value= symbol
        request.OrderID.value = orderid
        request.ClOrdID.value = clordid
        return request

    @classmethod
    def create_order_cancel_reject(cls,
                                   orderid,
                                   clordid,
                                   cancelrejreason=Fix.Tags.CxlRejReason.Values.TOO_LATE_TO_CANCEL,
                                   cancelrejresponseto=Fix.Tags.CxlRejResponseTo.Values.ORDER_CANCEL_REQUEST,
                                   cancelrejtext=""):
        report = Fix.Messages.OrderCancelReject()
        report.OrderID.value = orderid
        report.ClOrdID.value = clordid
        report.CxlRejReason.value = cancelrejreason
        report.CxlRejResponseTo.value = cancelrejresponseto
        report.Text.value = cancelrejtext

    @classmethod
    def create_request_for_position(cls,
                                    reqid):
        request = Fix.Messages.RequestForPositions()
        request.PosReqID.value = reqid
        return request

    @classmethod
    def create_position_report(cls,
                               reqid):
        report = Fix.Messages.PositionReport()
        report.PosReqID.value = reqid
        return report

    @classmethod
    def create_position_amount_data(cls, currency, amount, type=Fix.Tags.PosAmtType.Values.CASH_AMOUNT):
        """
        Create position amount data
        :param currency: Currency
        :param amount: Amount
        :param type: CASH_AMOUNT as total balance. FINAL_MARK_TO_MARKET_AMOUNT as available balance.
        :return: Repeating group of position amount data
        """
        group = Fix.Components.PositionAmountData.NoPosAmt()
        group.PositionCurrency.value = currency
        group.PosAmt.value = amount
        group.PosAmtType.value = type
        return group

