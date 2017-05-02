#!/usr/bin/python3
from bitz.realtime_strategy import RealTimeStrategy
from bitz.factory import Factory
from bitz.market_data import Snapshot
from bitz.FIX50SP2 import FIX50SP2 as Fix
import bitz.instrument as instrument
from bitz.util import update_fixtime, fixmsg2dict
from datetime import datetime, timedelta
from uuid import uuid4 as uuid
from typing import Tuple
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
    def __init__(self, name: str, ordsvr, logger, fiat_size=50):
        """
        Constructor
        """
        RealTimeStrategy.__init__(self, name, ordsvr, logger, fiat_size)
        self.target_instmt = instrument.Gatecoin_BTCHKD
        self.referenced_instmts = [instrument.Quoine_BTCUSD]
        self.profit_margin_fiat_currency = 100          # Profit margin between the best price and the market price
        self.fiat_size = fiat_size

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
                    bid *= self.target_instmt.fiat_rate
                    ask *= self.target_instmt.fiat_rate

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
            market_bid = int(market_bid / self.target_instmt.tick_size + 0.5) * self.target_instmt.tick_size
            if market_bid >= target_snapshot.order_book.b1 - self.target_instmt.tick_size:
                price = target_snapshot.order_book.b1 - self.target_instmt.tick_size
                qty = int(self.fiat_size / price / 0.0001 + 0.5) * 0.0001
                self.__init_new_order_single(order, price, qty)
                return True
            else:
                return False
        elif order.Side.value == Fix.Tags.Side.Values.SELL:
            market_ask = market_price + self.profit_margin_fiat_currency
            # Rounding
            market_ask = int(market_ask / self.target_instmt.tick_size + 0.5) * self.target_instmt.tick_size
            if market_ask <= target_snapshot.order_book.a1 - self.target_instmt.tick_size:
                price = target_snapshot.order_book.a1 - self.target_instmt.tick_size
                qty = int( self.fiat_size / price / 0.0001 + 0.5) * 0.0001
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

        self.logger.info(self.__class__.__name__, "Start monitoring the market...")

        while self.running:
            snapshot = self.ordsvr.get_latest_snapshot(0)

            # Flow back to the beginning of the loop if no snapshot is updated
            if snapshot is None:
                self.running = False
                continue
            elif snapshot == Snapshot.UpdateType.NONE:
                continue

            # Update target snapshot
            if target_snapshot is None:
                target_snapshot = self.ordsvr.get_exchange_snapshot(self.target_instmt.exchange, self.target_instmt.instmt_name)
                if target_snapshot is None:
                    continue

            # Calculate the market price
            # 1. If there is no open orders,
            #   a) Initialize the buy and sell order by the place_price
            #   b) Check the risk limit to decide which side can be placed
            #   c) Send the order to the order server. If the request succeeds, get the order ack.
            # 2. If there is open orders,
            #   a) Monitor if the order has been filled by whether the previous depth is same as the current one.
            #   b) If the market bid/ask is lower/larger than the placed bid/ask price, cancel the order.
            if open_order is not None:
                self.__init_order_status_request(order_status_request, open_order)
                fix_responses, err_text = self.ordsvr.request(order_status_request)
                assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                status = fix_responses[0]
                assert status.ExecType.value == Fix.Tags.ExecType.Values.ORDER_STATUS, \
                        "Unexpected ExecTYpe value (%s)" % status.ExecType.value
                if status.LeavesQty.value == 0:
                    # If the order has been fully filled
                    self.logger.info('test', fixmsg2dict(status))
                    break
                else:
                    # When the order has not been filled
                    is_cancel_order = False
                    if open_order.Side.value == Fix.Tags.Side.Values.BUY:
                        is_cancel_order = target_snapshot.order_book.b1 > open_order.Price.value
                    elif open_order.Side.value == Fix.Tags.Side.Values.SELL:
                        is_cancel_order = target_snapshot.order_book.a1 < open_order.Price.value
                    else:
                        raise NotImplementedError("Side %s not yet implemented." % open_order.Side.value)

                    # Cancel the order if the best bid exceeds the placed price
                    if is_cancel_order:
                        self.__init_order_cancel_reqeust(order_cancel_request, open_order)
                        fix_responses, err_text = self.ordsvr.request(order_cancel_request)
                        assert len(fix_responses) == 1, "Unexpected number of messages (%d)" % len(fix_responses)
                        response = fix_responses[0]

                        if response.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT and \
                            response.OrdStatus.value == Fix.Tags.OrdStatus.Values.CANCELED:
                            # Order is canceled
                            open_order = None
                            self.logger.info(self.__class__.__name__, "Cancel is accepted.\n" % fixmsg2dict(response))
                        elif response.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREJECT:
                            # Order is not canceled
                            self.logger.info(self.__class__.__name__, "Cancel is rejected.\n" % fixmsg2dict(response))

                    self.logger.info('test', '%s: Placed: %.4f / Market Price: %.4f' % (self.ordsvr.now_string(), status.Price.value, self.__calculate_market_price()[0]))
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
                    else:
                        # Order nack
                        self.logger.info(self.__class__.__name__, "Order is rejected.\n%s" % fixmsg2dict(response))
                else:
                    self.logger.info(self.__class__.__name__, "Error (%s) in placing orders." % err_text)

def get_args():
    """
    Get input arguments
    """
    parser = argparse.ArgumentParser(description='Single market marking.')
    parser.add_argument('-config', action='store', dest='config',
                        help='Configuration file path',
                        default='')
    return parser.parse_args()


def main():
    # Get input arguments
    args = get_args()

    # Create factory
    factory = Factory(args.config)

    # Logger
    logger = factory.create_logger()

    # Starting...
    logger.info('[main]', "Process is starting now...")

    # Initialize objects
    market_data_feed = factory.create_market_data_feed(logger)
    journal_db = factory.create_journal_database()
    realtime_db = factory.create_realtime_database()
    risk_manager = factory.create_risk_manager()
    order_server = factory.create_order_server(logger, journal_db, realtime_db, risk_manager, market_data_feed)

    # Register exchange
    order_server.register_exchange(factory.create_exchange('Gatecoin', market_data_feed=market_data_feed))

    # Initialize exchange risk
    order_server.initialize_exchange_risk()

    # Strategy initialization
    smm = SingleMarketMaking('SingleMarketMaking', order_server, logger)
    signal.signal(signal.SIGINT, smm.handle_signal)
    signal.signal(signal.SIGTERM, smm.handle_signal)
    smm.monitor()

    # Starting...
    logger.info('[main]', "Process has ended.")

if __name__ == '__main__':
    main()
