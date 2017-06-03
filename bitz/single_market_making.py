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
        SEEKING_FOR_A_BETTER_PRICE = 4

    class TradeSide:
        BOTH = 0
        BUY_ONLY = 1
        SELL_ONLY = 1

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
        self.default_trading_qty = 0.006
        self.default_trade_side = SingleMarketMaking.TradeSide.BOTH

        # Trading objects
        self.__open_orders = {}
        self.__target_snapshot = None
        self.__order_status_request = Fix.Messages.OrderStatusRequest()
        self.__order_cancel_request = Fix.Messages.OrderCancelRequest()

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
        if 'default_trading_qty' in kwargs.keys():
            self.default_trading_qty = kwargs['default_trading_qty']
        if 'default_trade_side' in kwargs.keys():
            default_trade_side = kwargs['default_trade_side']
            if default_trade_side >= 0 and default_trade_side <= 2:
                self.default_trade_side = default_trade_side
            else:
                raise NotImplementedError("Default trade side (%d) not implemented" % default_trade_side)

    def init_strategy(self):
        """
        Initialize strategy
        """
        # Initialize orders
        for side in [Fix.Tags.Side.Values.BUY, Fix.Tags.Side.Values.SELL]:
            if self.default_trade_side == SingleMarketMaking.TradeSide.BOTH or int(side) == self.default_trade_side:
                order = self.__create_new_order_single(self.target_instmt, side)
                self.__open_orders[order] = None

    def on_market_update(self, snapshot):
        """
        Callback when the market is updated.
        :param snapshot: Market data snapshot
        :return False for terminating running
        """
        # No open order and signaled to exit
        if not self.__check_any_open_position() and not self.running:
            return False

        # Flow back to the beginning of the loop if no snapshot is updated
        if snapshot is None:
            self.running = False
            return False
        elif snapshot == Snapshot.UpdateType.NONE and not self.__check_any_open_position():
            return True

        # Update target snapshot
        if self.__target_snapshot is None:
            self.__target_snapshot = self.ordsvr.get_exchange_snapshot(self.target_instmt.exchange, self.target_instmt.instmt_name)
            if self.__target_snapshot is None:
                return True
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
        for order, open_order in self.__open_orders.items():
            if open_order is not None:
                # Cancel the order if the order is still open and one of the following conditions is fulfilled
                # 1. Not at the best price
                # 2. Market status stalled for a while
                # 3. Program exit
                # 4. Too far from the second best price

                # Query the open order status
                if not self.__update_best_bid_ask_price(order, self.__target_snapshot.order_book):
                    self.__init_order_status_request(self.__order_status_request, open_order)
                    fix_responses, err_text = self.ordsvr.request(self.__order_status_request)
                    # Assert
                    assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                    open_order = fix_responses[0]
                    self.__open_orders[order] = open_order
                    assert open_order.ExecType.value == Fix.Tags.ExecType.Values.ORDER_STATUS, \
                        "Unexpected ExecTYpe value (%s)" % open_order.ExecType.value
                    # Check leaves qty
                    if open_order.LeavesQty.value == 0:
                        # If the order has been fully filled
                        self.logger.info(self.__class__.__name__, "Order is fully filled.\nFilled volume = %.4f.\n%s" % \
                                         (open_order.CumQty.value, fixmsg2dict(open_order)))
                        self.__open_orders[order] = None
                        return True

                cancel_reason = self.__check_cancel_condition(open_order)
                # Cancel the order if the best bid exceeds the placed price
                if cancel_reason != self.CancelReason.NONE:
                    self.__init_order_cancel_reqeust(self.__order_cancel_request, open_order)
                    self.__order_cancel_request.Text.value = cancel_reason
                    fix_responses, err_text = self.ordsvr.request(self.__order_cancel_request)
                    assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                    response = fix_responses[0]

                    if response.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT and \
                                    response.OrdStatus.value == Fix.Tags.OrdStatus.Values.CANCELED:
                        # Order is canceled
                        self.__open_orders[order] = None
                        self.logger.info(self.__class__.__name__, "Cancel is accepted.\n%s" % fixmsg2dict(response))
                    elif response.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREJECT:
                        # Order is not canceled
                        self.rejected_request += 1
                        self.logger.info(self.__class__.__name__, "Cancel is rejected.\n%s" % fixmsg2dict(response))

            else:
                if self.__is_place_order(order) and self.ordsvr.valid_risk_limit(order):
                    fix_responses, err_text = self.ordsvr.request(order)
                else:
                    return True

                # Check the placement response
                if err_text == "":
                    assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                    response = fix_responses[0]     # Order ack/nack
                    if response.ExecType.value == Fix.Tags.ExecType.Values.NEW:
                        # Order ack
                        self.__open_orders[order] = response
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
            return False

        return True

    def __check_any_open_position(self):
        """
        Check if there is any open position
        :return: True if any open position
        """
        for request, response in self.__open_orders.items():
            if response is not None:
                return True
        return False

    def __create_request_id(self):
        """
        Create request id
        :return: Request id
        """
        return self.ordsvr.now_string() + str(uuid())

    def __create_new_order_single(self, instmt: Instrument, side) -> Fix.Messages.NewOrderSingle:
        """
        Create a new order single message
        :param instmt: Instrument
        :param side: Side
        :return: NewOrderSingle message
        """
        new_order_single = Fix.Messages.NewOrderSingle()
        new_order_single.Instrument.Symbol.value = instmt.instmt_name
        new_order_single.Instrument.SecurityExchange.value = instmt.exchange
        new_order_single.Price.value = 0
        new_order_single.ClOrdID.value = ''
        new_order_single.OrderQtyData.OrderQty.value = 0
        new_order_single.OrdType.value = Fix.Tags.OrdType.Values.LIMIT
        new_order_single.TimeInForce.value = Fix.Tags.TimeInForce.Values.DAY
        new_order_single.Side.value = side
        new_order_single.TriggeringInstruction.TriggerPrice.value = 0
        new_order_single.TriggeringInstruction.TriggerNewQty.value = 0

        # Append strategy group
        group = new_order_single.StrategyParametersGrp.NoStrategyParameters()
        group.StrategyParameterName.value = "best_bid"
        group.StrategyParameterType.value = group.StrategyParameterType.Values.FLOAT
        group.StrategyParameterValue.value = 0.0
        new_order_single.StrategyParametersGrp.groups.append(group)

        group = new_order_single.StrategyParametersGrp.NoStrategyParameters()
        group.StrategyParameterName.value = "best_ask"
        group.StrategyParameterType.value = group.StrategyParameterType.Values.FLOAT
        group.StrategyParameterValue.value = 0.0
        new_order_single.StrategyParametersGrp.groups.append(group)

        return new_order_single

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
        status_request.Header.SendingTime.value = self.ordsvr.now_string()

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
        order_cancel.OrderQtyData.OrderQty.value = last_status.OrderQtyData.OrderQty.value
        order_cancel.Header.SendingTime.value = self.ordsvr.now_string()

    def __init_new_order_single(self, order_book, new_order_single: Fix.Messages.NewOrderSingle, price, qty):
        """
        Create new order single
        :return: New order single
        """
        now_string = self.ordsvr.now_string()
        new_order_single.Price.value = price
        new_order_single.OrderQtyData.OrderQty.value = qty
        new_order_single.ClOrdID.value = self.__create_request_id()
        new_order_single.TransactTime.value = now_string
        new_order_single.Header.SendingTime.value = now_string

        # Set triggering quantity. If the price is not with the first 5 price range,
        # set it as 0 for triggering quantity.
        new_order_single.TriggeringInstruction.TriggerPrice.value = price
        new_order_single.TriggeringInstruction.TriggerNewQty.value = 0

        # Strategy group
        self.__update_best_bid_ask_price(new_order_single, order_book)

    def __update_best_bid_ask_price(self, new_order_single, order_book):
        """
        Update best bid and ask price at the new order single order
        :param new_order_single: New order single
        :param order_book: Order book
        """
        is_updated = True
        for group in new_order_single.StrategyParametersGrp.groups:
            if group.StrategyParameterName.value == "best_bid":
                if group.StrategyParameterValue.value != order_book.b1:
                    group.StrategyParameterValue.value = order_book.b1
                    is_updated = False
            elif group.StrategyParameterName.value == "best_ask":
                if group.StrategyParameterValue.value != order_book.a1:
                    group.StrategyParameterValue.value = order_book.a1
                    is_updated = False

        return is_updated

    def __calculate_market_price(self, side):
        """
        Calculate market price
        :return: Tuple of best bid and ask. If no market price is calculated, None is returned
        """
        is_valid = True
        if side == Fix.Tags.Side.Values.BUY:
            best_price = 1e9
        elif side == Fix.Tags.Side.Values.SELL:
            best_price = 0
        else:
            raise NotImplementedError("Side (%s) not yet implemented." % side)

        for instmt in self.referenced_instmts:
            snapshot = self.ordsvr.get_exchange_snapshot(instmt.exchange, instmt.instmt_name)
            if snapshot is None:
                # Return if any instrument is not prepared
                is_valid = False
                break
            else:
                px = snapshot.order_book.b1 if side == Fix.Tags.Side.Values.BUY else snapshot.order_book.a1

                if px > 0:
                    px *= self.target_instmt.usd_rate
                    best_price = min(px, best_price) if side == Fix.Tags.Side.Values.BUY else max(px, best_price)
                else:
                    # Return if any side of the prices is not prepared
                    is_valid = False
                    break

        if is_valid:
            return best_price
        else:
            return None

    def __is_place_order(self, order: Fix.Messages.NewOrderSingle):
        """
        Check if create a new order
        :param market_price: Market price on the side
        :param order: Order
        :return: Tur if passed
        """
        assert self.__target_snapshot is not None, "Target snapshot should not be none."
        market_price = self.__calculate_market_price(order.Side.value)
        side = order.Side.value

        if market_price is None:
            return False

        last_update_time = max(self.__target_snapshot.order_book.date_time, self.__target_snapshot.last_trade.date_time)
        if (self.ordsvr.now() - last_update_time).total_seconds() > self.market_data_stalled_time_sec:
            return False

        if side == Fix.Tags.Side.Values.BUY:
            market_price -= self.profit_margin_fiat_currency
            market_price = int(market_price / self.target_instmt.price_min_size + 0.5) * self.target_instmt.price_min_size
            if market_price >= self.__target_snapshot.order_book.b1 + self.aggressiveness * self.target_instmt.price_min_size and \
                            self.__target_snapshot.order_book.b1 > 0:
                price = self.__target_snapshot.order_book.b1 + self.aggressiveness * self.target_instmt.price_min_size
                qty = self.default_trading_qty
                self.__init_new_order_single(self.__target_snapshot.order_book, order, price, qty)
                return True
            else:
                return False
        elif side == Fix.Tags.Side.Values.SELL:
            market_price += self.profit_margin_fiat_currency
            # Rounding
            market_price = int(market_price / self.target_instmt.price_min_size + 0.5) * self.target_instmt.price_min_size
            if market_price <= self.__target_snapshot.order_book.a1 - self.aggressiveness * self.target_instmt.price_min_size and \
                            market_price > 0:
                price = self.__target_snapshot.order_book.a1 - self.aggressiveness * self.target_instmt.price_min_size
                qty = self.default_trading_qty
                self.__init_new_order_single(self.__target_snapshot.order_book, order, price, qty)
                return True
            else:
                return False
        else:
            raise NotImplementedError("Side %s not yet implemented." % side)

    def __check_cancel_condition(self, open_order):
        """
        Check cancel condition
        :return: Cancel condition
        """
        assert self.__target_snapshot is not None, "Target snapshot should not be none."
        cancel_reason = self.CancelReason.NONE
        # Check condition 1
        if open_order.Side.value == Fix.Tags.Side.Values.BUY:
            if self.__target_snapshot.order_book.b1 > open_order.Price.value:
                cancel_reason = self.CancelReason.NOT_AT_THE_BEST_PRICE
        elif open_order.Side.value == Fix.Tags.Side.Values.SELL:
            if self.__target_snapshot.order_book.a1 < open_order.Price.value:
                cancel_reason = self.CancelReason.NOT_AT_THE_BEST_PRICE
        else:
            raise NotImplementedError("Side %s not yet implemented." % open_order.Side.value)
        # Check condition 2
        last_update_time = max(self.__target_snapshot.order_book.date_time, self.__target_snapshot.last_trade.date_time)
        if (self.ordsvr.now() - last_update_time).total_seconds() > self.market_data_stalled_time_sec:
            cancel_reason = self.CancelReason.STALLED_FOR_LONG

        # Check condition 3
        if not self.running:
            cancel_reason = self.CancelReason.PROGRAM_EXIT

        # Check condition 4
        market_price = self.__calculate_market_price(open_order.Side.value)
        if open_order.Side.value == Fix.Tags.Side.Values.BUY:
            if market_price > self.__target_snapshot.order_book.b2 and market_price < open_order.Price.value:
                cancel_reason = self.CancelReason.SEEKING_FOR_A_BETTER_PRICE
        elif open_order.Side.value == Fix.Tags.Side.Values.SELL:
            if market_price < self.__target_snapshot.order_book.a2 and market_price > open_order.Price.value:
                cancel_reason = self.CancelReason.NOT_AT_THE_BEST_PRICE
        else:
            raise NotImplementedError("Side %s not yet implemented." % open_order.Side.value)

        return cancel_reason

