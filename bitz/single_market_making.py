#!/usr/bin/python3
from bitz.realtime_strategy import RealTimeStrategy
from bitz.market_data import Snapshot
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.util import update_fixtime, fixmsg2dict
from bitz.instrument import Instrument
from uuid import uuid4 as uuid
from typing import Tuple, List

from json import dumps
import signal
import argparse
import sys

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser


class SingleMarketMaking(RealTimeStrategy):
    """
    Single market marking
    """
    class CancelReason:
        NONE = 0
        NOT_AT_THE_BEST_PRICE = 1
        STALLED_FOR_LONG = 2
        PROGRAM_EXIT = 3

    def __init__(self, name: str, ordsvr, logger, target_instmt: Instrument, referenced_instmt: List[Instrument]):
        """
        Constructor
        """
        RealTimeStrategy.__init__(self, name, ordsvr, logger)
        self.target_instmt = target_instmt
        self.referenced_instmts = referenced_instmt
        self.profit_margin_fiat_currency = 100          # Profit margin between the best price and the market price
        self.aggressiveness = 1                         # Number of ticks place above the best price
        self.rejected_request = 0
        self.max_rejected_request = 10
        self.market_data_stalled_time_sec = 30 * 60
        self.max_fiat_currency_risk = 50

    def init_parameters(self, **kwargs):
        """
        Initialize parameters
        :param kwargs: Parameters
        """
        if 'profit_margin_fiat_currency' in kwargs.keys():
            self.profit_margin_fiat_currency = kwargs['profit_margin_fiat_currency']
        if 'aggressiveness' in kwargs.keys():
            self.aggressiveness = kwargs['aggressiveness']
        if 'max_rejected_request' in kwargs.keys():
            self.max_rejected_request = kwargs['max_rejected_request']
        if 'market_data_stalled_time_sec' in kwargs.keys():
            self.market_data_stalled_time_sec = kwargs['market_data_stalled_time_sec']
        if 'max_fiat_currency_risk' in kwargs.keys():
            self.max_fiat_currency_risk = kwargs['max_fiat_currency_risk']


    def __create_request_id(self):
        """
        Create request id
        :return: Request id
        """
        return self.ordsvr.now_string() + str(uuid())

    def __init_order_status_request(self,
                                    status_request: Fix.Messages.OrderStatusRequest,
                                    last_status: Fix.Messages.ExecutionReport):
        """
        Initialize the order status request by the last execution report
        :param status_request: Order status request
        :param last_status: Last execution report
        """
        status_request.OrdStatusReqID.value = self.__create_request_id()
        status_request.OrderID.value = last_status.OrderID.value
        status_request.Instrument.Symbol.value = last_status.Instrument.Symbol.value
        status_request.Instrument.SecurityExchange.value = last_status.Instrument.SecurityExchange.value
        status_request.Side.value = last_status.Side.value

    def __init_order_cancel_reqeust(self,
                                    order_cancel: Fix.Messages.OrderCancelRequest,
                                    last_status: Fix.Messages.ExecutionReport):
        """
        Initialize the order cancel request by the last execution report
        :param order_cancel: Order cancel request
        :param last_status: Last execution report
        """
        order_cancel.ClOrdID.value = self.__create_request_id()
        order_cancel.OrderID.value = last_status.OrderID.value
        order_cancel.Instrument.Symbol.value = last_status.Instrument.Symbol.value
        order_cancel.Instrument.SecurityExchange.value = last_status.Instrument.SecurityExchange.value
        order_cancel.Side.value = last_status.Side.value


    def __init_new_order_single(self, new_order_single: Fix.Messages.NewOrderSingle, price, qty):
        """
        Create new order single
        :return: New order single
        """
        new_order_single.Instrument.Symbol.value = self.target_instmt.instmt_name
        new_order_single.Instrument.SecurityExchange.value = self.target_instmt.exchange
        new_order_single.Price.value = price
        new_order_single.ClOrdID.value = self.__create_request_id()
        new_order_single.OrderQtyData.OrderQty.value = qty
        new_order_single.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        new_order_single.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY

        # Set triggering quantity. If the price is not with the first 5 price range,
        # set it as 0 for triggering quantity.
        new_order_single.TriggeringInstruction.TriggerPrice.value = price
        new_order_single.TriggeringInstruction.TriggerNewQty.value = 0

    def __calculate_market_price(self) -> Tuple[float, float]:
        """
        Calculate market price
        :return: Tuple of best bid and ask. If no market price is calculated, None is returned
        """
        is_valid = True
        best_bid = 1e9
        best_ask = 0

        for instmt in self.referenced_instmts:
            snapshot = self.ordsvr.get_exchange_snapshot(instmt.exchange, instmt.instmt_name)
            if snapshot is None:
                # Return if any instrument is not prepared
                is_valid = False
                break
            else:
                bid = snapshot.order_book.b1
                ask = snapshot.order_book.a1

                if bid > 0 and ask > 0:
                    bid *= self.target_instmt.usd_rate
                    ask *= self.target_instmt.usd_rate

                    best_bid = min(bid, best_bid)
                    best_ask = max(ask, best_ask)
                else:
                    # Return if any side of the prices is not prepared
                    is_valid = False
                    break

        if is_valid:
            return best_bid, best_ask
        else:
            return None, None
    def __is_place_order(self, market_price, order: Fix.Messages.NewOrderSingle):
        """
        Check if create a new order
        :param market_price: Market price on the side
        :param order: Order
        :return: Tur if passed
        """
        target_snapshot = self.ordsvr.get_exchange_snapshot(self.target_instmt.exchange, self.target_instmt.instmt_name)
        if order.Side.value == Fix.Tags.Side.Values.BUY:
            market_bid = market_price - self.profit_margin_fiat_currency
            market_bid = int(market_bid / self.target_instmt.price_min_size + 0.5) * self.target_instmt.price_min_size
            if market_bid >= target_snapshot.order_book.b1 + self.aggressiveness * self.target_instmt.price_min_size:
                price = target_snapshot.order_book.b1 + self.aggressiveness * self.target_instmt.price_min_size
                qty = int(self.max_fiat_currency_risk / price / self.target_instmt.qty_min_size) * self.target_instmt.qty_min_size
                self.__init_new_order_single(order, price, qty)
                return True
            else:
                return False
        elif order.Side.value == Fix.Tags.Side.Values.SELL:
            market_ask = market_price + self.profit_margin_fiat_currency
            # Rounding
            market_ask = int(market_ask / self.target_instmt.price_min_size + 0.5) * self.target_instmt.price_min_size
            if market_ask <= target_snapshot.order_book.a1 - self.aggressiveness * self.target_instmt.price_min_size:
                price = target_snapshot.order_book.a1 - self.aggressiveness * self.target_instmt.price_min_size
                qty = int( self.max_fiat_currency_risk / price / self.target_instmt.qty_min_size) * self.target_instmt.qty_min_size
                self.__init_new_order_single(order, price, qty)
                return True
            else:
                return False
        else:
            raise NotImplementedError("Side %s not yet implemented." % order.Side.value)

    def monitor(self):
        """
        Monitor the market
        """
        # Register strategy
        self.ordsvr.register_strategy(self, self.target_instmt)
        # Initialize orders
        buy_order = Fix.Messages.NewOrderSingle()
        sell_order = Fix.Messages.NewOrderSingle()
        order_status_request = Fix.Messages.OrderStatusRequest()
        order_cancel_request = Fix.Messages.OrderCancelRequest()
        buy_order.Side.value = Fix.Tags.Side.Values.BUY
        sell_order.Side.value = Fix.Tags.Side.Values.SELL
        target_snapshot = None
        open_order = None
        last_target_best_price = (0, 0)

        self.logger.info(self.__class__.__name__, "Start monitoring the market...")

        while True:
            snapshot = self.ordsvr.get_latest_snapshot(200000)

            # No open order and signaled to exit
            if open_order is None and not self.running:
                break

            # Flow back to the beginning of the loop if no snapshot is updated
            if snapshot is None:
                self.running = False
                break
            elif snapshot == Snapshot.UpdateType.NONE and open_order is None:
                continue

            # Update target snapshot
            if target_snapshot is None:
                target_snapshot = self.ordsvr.get_exchange_snapshot(self.target_instmt.exchange, self.target_instmt.instmt_name)
                if target_snapshot is None:
                    continue
                else:
                    self.logger.info(self.__class__.__name__,
                                     "Target instrument %s/%s has received the first snapshot" % \
                                     (self.target_instmt.exchange, self.target_instmt.instmt_name))

            # Calculate the market price
            # 1. If there is no open orders,
            #   a) Initialize the buy and sell order by the place_price
            #   b) Check the risk limit to decide which side can be placed
            #   c) Send the order to the order server. If the request succeeds, get the order ack.
            # 2. If there is open orders,
            #   a) Monitor if the order has been filled by when the previous depth is different from the current one
            #   b) If the market bid/ask is lower/larger than the placed bid/ask price, cancel the order.
            if open_order is not None:
                # Query the order status only when the order book has been changed
                if open_order.Side.value == Fix.Tags.Side.Values.BUY:
                    if target_snapshot.order_book.b1 != last_target_best_price[0] or  \
                        target_snapshot.order_book.bq1 != last_target_best_price[1]:
                        is_query_status = True
                    else:
                        is_query_status = False
                elif open_order.Side.value == Fix.Tags.Side.Values.SELL:
                    if target_snapshot.order_book.a1 != last_target_best_price[0] or \
                                    target_snapshot.order_book.aq1 != last_target_best_price[1]:
                        is_query_status = True
                    else:
                        is_query_status = False
                else:
                    raise NotImplementedError("Side (%s) not yet implemented." % open_order.Side.value)

                # Query the open order status
                if is_query_status:
                    self.__init_order_status_request(order_status_request, open_order)
                    fix_responses, err_text = self.ordsvr.request(order_status_request)
                    # Assert
                    assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                    open_order = fix_responses[0]
                    assert open_order.ExecType.value == Fix.Tags.ExecType.Values.ORDER_STATUS, \
                            "Unexpected ExecTYpe value (%s)" % open_order.ExecType.value
                    # Check leaves qty
                    if open_order.LeavesQty.value == 0:
                        # If the order has been fully filled
                        self.logger.info(self.__class__.__name__, "Order is fully filled.\nFilled volume = %.4f.\n%s" % \
                                         (open_order.CumQty.value, fixmsg2dict(open_order)))
                        open_order = None
                        last_target_best_price = (0, 0)
                        continue
                    else:
                        if open_order.Side.value == Fix.Tags.Side.Values.BUY:
                            last_target_best_price = (target_snapshot.order_book.b1, target_snapshot.order_book.bq1)
                        elif open_order.Side.value == Fix.Tags.Side.Values.SELL:
                            last_target_best_price = (target_snapshot.order_book.a1, target_snapshot.order_book.aq1)
                        else:
                            raise NotImplementedError("Side (%s) not yet implemented." % open_order.Side.value)

                # Cancel the order if the order is still open and one of the following conditions is fulfilled
                # 1. Not at the best price
                # 2. Market status stalled for a while
                # 3. Program exit
                cancel_reason = self.CancelReason.NONE
                # Check condition 1
                if open_order.Side.value == Fix.Tags.Side.Values.BUY:
                    if target_snapshot.order_book.b1 > open_order.Price.value:
                        cancel_reason = self.CancelReason.NOT_AT_THE_BEST_PRICE
                elif open_order.Side.value == Fix.Tags.Side.Values.SELL:
                    if target_snapshot.order_book.a1 < open_order.Price.value:
                        cancel_reason = self.CancelReason.NOT_AT_THE_BEST_PRICE
                else:
                    raise NotImplementedError("Side %s not yet implemented." % open_order.Side.value)
                # Check condition 2
                last_update_time = max(target_snapshot.order_book.date_time, target_snapshot.last_trade.date_time)
                if (self.ordsvr.now() - last_update_time).total_seconds() > self.market_data_stalled_time_sec:
                    cancel_reason = self.CancelReason.STALLED_FOR_LONG
                # Check condition 3
                if not self.running:
                    cancel_reason = self.CancelReason.PROGRAM_EXIT

                # Cancel the order if the best bid exceeds the placed price
                if cancel_reason != self.CancelReason.NONE:
                    self.__init_order_cancel_reqeust(order_cancel_request, open_order)
                    order_cancel_request.Text.value = cancel_reason
                    fix_responses, err_text = self.ordsvr.request(order_cancel_request)
                    assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                    response = fix_responses[0]

                    if response.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT and \
                        response.OrdStatus.value == Fix.Tags.OrdStatus.Values.CANCELED:
                        # Order is canceled
                        open_order = None
                        self.logger.info(self.__class__.__name__, "Cancel is accepted.\n%s" % fixmsg2dict(response))
                    elif response.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREJECT:
                        # Order is not canceled
                        self.rejected_request += 1
                        self.logger.info(self.__class__.__name__, "Cancel is rejected.\n%s" % fixmsg2dict(response))
            else:
                market_bid, market_ask = self.__calculate_market_price()
                if self.__is_place_order(market_bid, buy_order) and \
                    self.ordsvr.valid_risk_limit(buy_order, self):
                    fix_responses, err_text = self.ordsvr.request(buy_order)
                elif self.__is_place_order(market_ask, sell_order) and \
                        self.ordsvr.valid_risk_limit(sell_order, self):
                    fix_responses, err_text = self.ordsvr.request(sell_order)
                else:
                    continue

                # Check the placement response
                if err_text == "":
                    assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                    response = fix_responses[0]     # Order ack/nack
                    if response.ExecType.value == Fix.Tags.ExecType.Values.NEW:
                        # Order ack
                        open_order = response
                        self.logger.info(self.__class__.__name__, "Order is opened.\n%s" % fixmsg2dict(response))
                    elif response.ExecType.value == Fix.Tags.ExecType.Values.REJECTED:
                        # Order nack
                        self.rejected_request += 1
                        self.logger.info(self.__class__.__name__, "Order is rejected.\n%s" % fixmsg2dict(response))
                    else:
                        raise NotImplementedError("Not implemented ExecType (%s)" % response.ExecType.value)
                else:
                    self.logger.info(self.__class__.__name__, "Error (%s) in placing orders." % err_text)

            if self.rejected_request > self.max_rejected_request:
                self.logger.error(self.__class__.__name__, "Number of rejected request (%d) has already exceeded." % self.rejected_request)
                break
