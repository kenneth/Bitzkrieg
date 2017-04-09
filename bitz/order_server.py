#!/usr/bin/python3
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.util import update_fixtime, fixmsg2dict
from datetime import datetime

class OrderServer:
    """
    Order server

    The server maintains the following:
    1. House order book
    2. Risk level and limit
    3. Exchange interface
    4. Archive all the incoming and outgoing messages

    # ClOrdID - Set by the strategy/source
    # SecondaryClOrdID - Set by the order server
    # OrderID - Set by the gateway, indicating the exchange order ID

    All the communication is via FIX protocol.
    """
    def __init__(self, request_database, response_database, logger, data_feed):
        """
        Constructor
        """
        self.request_database = request_database
        self.response_database = response_database
        self.logger = logger
        self.data_feed = data_feed
        self.exchanges = {}
        self.exchange_risk_exposure = {}
        self.strategy_risk_exposure = {}
        self.strategy_open_orders = {}
        self.current_order_id = int(datetime.utcnow().strftime("%Y%m%d%H%M%S")) * 100
        self.current_exec_id = 0

    @classmethod
    def assert_msgtype(cls, msg, expect):
        """
        Assert MsgType
        """
        assert msg.MsgType == expect, "Invalid MsgType (%s). Expected MsgType %s" % \
               (msg.MsgType, expect)

    def assert_exchange(self, exchange_name, value=True):
        """
        Assert exchange name
        """
        assert value == (exchange_name in self.exchanges.keys()), \
            "Duplicated registration of exchange %s" % exchange_name
        assert value == (exchange_name in self.exchange_risk_exposure.keys()), \
            "Duplicated registration of exchange %s" % exchange_name

    def assert_strategy(self, strategy, value=True):
        """
        Assert strategy
        """
        assert value == (strategy in self.strategy_risk_exposure.keys()), \
               "Duplicated strategy %s" % strategy.get_name()
        assert value == (strategy in self.strategy_open_orders.keys()), \
               "Duplicated strategy %s" % strategy.get_name()

    def get_next_order_id(self):
        """
        Get the next order id
        """
        self.current_order_id += 1
        return self.current_order_id

    def get_next_exec_id(self):
        """
        Get the next exec id
        """
        self.current_exec_id += 1
        return self.current_exec_id

    def register_gateway(self, exchange_name, exchange_server):
        """
        Register a gateway
        """
        self.assert_exchange(exchange_name, False)
        self.exchanges[exchange_name] = exchange_server
        self.exchange_risk_exposure[exchange_name] = { "Balance": {}, \
                                                       "AvailableBalance" : {}}
        self.logger.info(self.__class__.__name__,
                         "Exchange %s has been registered.\nExchange list: %s" % \
                         (exchange_name, self.exchanges.keys()))

    def register_strategy(self, strategy):
        """
        Register a staregy
        """
        self.assert_strategy(strategy, False)
        self.strategy_risk_exposure[strategy] = {}      # Key is the field name, value is the double
        self.strategy_open_orders[strategy] = {}        # Key is the order id, value is the ER
        self.logger.info(self.__class__.__name__,
                         "Strategy %s has been registered.\nStrategy list: %s" % \
                         (strategy.get_name(), [s.get_name() for s in self.strategy_risk_exposure.keys()]))

    def insert_response_database(self, msg):
        """
        Insert response to database
        """
        if msg.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
            self.response_database.insert("%s-%05d-%s" % (msg.SecondaryClOrdID.value, msg.ExecID.value, msg.MsgType),
                              fixmsg2dict(msg))
        elif msg.MsgType == Fix.Tags.MsgType.Values.POSITIONREPORT:
            self.response_database.insert("%s-%05d-%s" % \
                (msg.PosReqID.value, msg.PosMaintRptID.value, msg.MsgType), fixmsg2dict(msg))
        else:
            assert False, "Invalid MsgType %s" % msg.MsgType

    def allow_strategy_risk_exposure(self, source, msg):
        """
        Check from the strategy risk exposure if the order is allowed to be placed
        """
        self.assert_strategy(source)
        if msg.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            exposure = msg.OrderQtyData.OrderQty.value
            side = msg.Side.value

            if side == Fix.Tags.Side.Values.BUY and \
                self.strategy_risk_exposure[source]["open_bid_amt"] + exposure > \
                self.strategy_risk_exposure[source]["max_bid_amt"]:
                return False
            elif side == Fix.Tags.Side.Values.SELL and \
                self.strategy_risk_exposure[source]["open_ask_amt"] + exposure > \
                self.strategy_risk_exposure[source]["max_ask_amt"]:
                return False
            else:
                return True
        else:
            assert False, "MsgType (%s) is not supported yet." % msg.MsgType

    def update_strategy_risk_exposure(self, source, msg):
        """
        Update the strategy risk exposure
        """
        self.assert_strategy(source)
        if msg.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
            exposure = msg.OrderQtyData.OrderQty.value
            side = msg.Side.value
            execType = msg.ExecType.value

            if execType == Fix.Tags.ExecType.Values.NEW:
                self.strategy_risk_exposure[source]["open_bid_amt"] += exposure if side == Fix.Tags.Side.Values.BUY else 0
                self.strategy_risk_exposure[source]["open_ask_amt"] += exposure if side == Fix.Tags.Side.Values.SELL else 0
            elif execType == Fix.Tags.ExecType.Values.CANCELED:
                self.strategy_risk_exposure[source]["open_bid_amt"] -= exposure if side == Fix.Tags.Side.Values.BUY else 0
                self.strategy_risk_exposure[source]["open_ask_amt"] -= exposure if side == Fix.Tags.Side.Values.SELL else 0
            else:
                assert False, "Not supported ExecType (%s)" % execType
        else:
            assert False, "MsgType (%s) is not supported yet." % msg.MsgType

    def query_risk_exposure(self):
        """
        Query the risk exposure among all exchanges and strategies
        """
        for name, exchange in self.exchanges.items():
            req = Fix.Messages.RequestForPositions()
            update_fixtime(req, Fix.Tags.SendingTime.Tag)
            req.PosReqID.value = "%sQPOS" % self.get_next_order_id()
            req.Instrument.SecurityExchange.value = name
            self.request(self, req)

    def request(self, source, msg):
        """
        Request
        """
        exchange_name = msg.Instrument.SecurityExchange.value
        self.assert_exchange(exchange_name)

        if msg.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            ##################################################
            # Handle add order
            ##################################################
            self.assert_strategy(source)

            # Add latency trip
            update_fixtime(msg, Fix.Tags.HopSendingTime.Tag, "OrdSvrOut")

            # Prepare the execution report
            ordsvr_response = self.__prepare_execution_report(msg, self.get_next_order_id(), self.get_next_exec_id())

            # Store request into the database
            self.request_database.insert(msg.ClOrdID.value, fixmsg2dict(msg))

            # Risk check first
            if self.allow_strategy_risk_exposure(source, msg):
                # Send it to the exchange
                gw_responses, error_msg = self.exchanges[exchange_name].request(msg)
                for gw_response in gw_responses:
                    self.assert_msgtype(gw_response, Fix.Tags.MsgType.Values.EXECUTIONREPORT)
                    if gw_response.ExecType.value == Fix.Tags.ExecType.Values.NEW:
                        # New order
                        ordsvr_response.ExecType.value = Fix.Tags.ExecType.Values.NEW
                        ordsvr_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
                        # Update risk exposure
                        self.update_strategy_risk_exposure(source, ordsvr_response)
                        # Order ID
                        ordsvr_response.OrderID.value = gw_response.OrderID.value
                        # TransactTime
                        ordsvr_response.TransactTime.value = gw_response.TransactTime.value
                        # Update strategy open orders
                        assert ordsvr_response.SecondaryClOrdID.value not in self.strategy_open_orders[source].keys(), \
                               "Duplicated key (%s) in strategy_open_orders" % ordsvr_response.SecondaryClOrdID
                        self.strategy_open_orders[source][ordsvr_response.SecondaryClOrdID.value] = ordsvr_response
                    elif gw_response.ExecType.value == Fix.Tags.ExecType.Values.REJECTED:
                        # Reject order
                        ordsvr_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
                        ordsvr_response.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
                        # Rejection Text
                        ordsvr_response.Text.value = gw_response.Text
                        # Rejection Reason
                        ordsvr_response.OrdRejReason.value = gw_response.OrdRejReason
                        # LeavesQty
                        ordsvr_response.LeavesQty.value = 0
                        # TransactTime
                        ordsvr_response.TransactTime.value = gw_response.TransactTime.value
                    else:
                        assert False, "Not implemented other ExecType %s" % gw_response.ExecType.value
            else:
                # Reject order
                ordsvr_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
                ordsvr_response.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
                # Rejection Text
                curr_risk = self.strategy_risk_exposure[source]["open_bid_amt"] if msg.Side.value == Fix.Tags.Side.Values.BUY else\
                            self.strategy_risk_exposure[source]["open_ask_amt"]
                risk_limit = self.strategy_risk_exposure[source]["max_bid_amt"] if msg.Side.value == Fix.Tags.Side.Values.BUY else\
                            self.strategy_risk_exposure[source]["max_ask_amt"]

                ordsvr_response.Text.value = "Expected risk exposure (%.6f+%.6f) will exceed the risk limit (%.6f)" % \
                        (curr_risk, msg.OrderQtyData.OrderQty.value, risk_limit)
                # LeavesQty
                ordsvr_response.LeavesQty.value = 0

            # Add latency trip
            update_fixtime(ordsvr_response, Fix.Tags.SendingTime.Tag)
            update_fixtime(ordsvr_response, Fix.Tags.HopSendingTime.Tag, "OrdSvrIn")

            # Store response into the database
            self.insert_response_database(ordsvr_response)

            return ordsvr_response

        elif msg.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            self.assert_strategy(source)
            assert msg.SecondaryClOrdID.value in self.strategy_open_orders[source].keys(), \
                "SecondaryClOrdID %s cannot be found in source %s" % \
                (msg.SecondaryClOrdID.value, source.get_name())
            original_order = self.strategy_open_orders[source][msg.SecondaryClOrdID.value]
            original_order.ExecID.value = self.get_next_exec_id()

            # Add latency trip
            update_fixtime(msg, Fix.Tags.HopSendingTime.Tag, "OrdSvrOut")

            # Store request into the database
            self.request_database.insert(msg.ClOrdID.value, fixmsg2dict(msg))

            # Send it to the exchange
            gw_responses, error_msg = self.exchanges[exchange_name].request(msg)
            assert len(gw_responses) == 1, "More than 1 responses from the gateway (%d)" % \
                len(gw_responses)

            gw_response = gw_responses[0]
            if gw_response.MsgType == Fix.Tags.MsgType.Values.EXECUTIONREPORT:
                if gw_response.OrdStatus.value == Fix.Tags.OrdStatus.Values.CANCELED and \
                   gw_response.ExecType.value == Fix.Tags.ExecType.Values.CANCELED:
                    # Order is canceled
                    original_order.OrdStatus.value = Fix.Tags.OrdStatus.Values.CANCELED
                    original_order.ExecType.value = Fix.Tags.ExecType.Values.CANCELED
                    # Update risk exposure
                    self.update_strategy_risk_exposure(source, original_order)
                    # LeavesQty
                    original_order.LeavesQty.value = 0
                else:
                    assert False, "Invalid OrdStatus(%s) and ExecType (%s)" % \
                    (gw_response.OrdStatus.value, gw_response.ExecType.value)
            elif gw_respose.MsgType == Fix.Tags.MsgType.Values.ORDERCANCELREJECT:
                # Order is rejected
                original_order.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
                # Rejection text
                original_order.Text.value = error_msg
                # Rejection Reason
                original_order.OrdRejReason.value = gw_response.CxlRejReason.value

            # Add latency trip
            update_fixtime(original_order, Fix.Tags.HopSendingTime.Tag, "OrdSvrIn")

            # Store response into the database
            self.insert_response_database(original_order)

            return original_order

        elif msg.MsgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            ##################################################
            # Handle request for positions
            ##################################################
            # Add latency trip
            update_fixtime(msg, Fix.Tags.HopSendingTime.Tag, "OrdSvr")

            # Store request into the database
            self.request_database.insert(msg.PosReqID.value, fixmsg2dict(msg))

            gw_responses, error = self.exchanges[exchange_name].request(msg)
            for gw_response in gw_responses:
                self.assert_msgtype(gw_response, Fix.Tags.MsgType.Values.POSITIONREPORT)
                gw_response.PosMaintRptID.value = self.get_next_exec_id()
                gw_response.PosReqID.value = msg.PosReqID.value
                update_fixtime(gw_response, Fix.Tags.HopSendingTime.Tag, "OrdSvr")
                self.insert_response_database(gw_response)
                self.__handle_position_report(gw_response)

            # OrdSvr handles it. No output
            return None
        elif msg.MsgType == Fix.Tags.MsgType.Values.ORDERMASSSTATUSREQUEST:
            ##################################################
            # Handle mass status request
            ##################################################
            self.assert_strategy(source)
            open_orders = self.strategy_open_orders[source]

            # Add latency trip
            update_fixtime(msg, Fix.Tags.HopSendingTime.Tag, "OrdSvrOut")

            # Store request into the database
            self.request_database.insert(msg.MassStatusReqID.value, fixmsg2dict(msg))

            # Forward the query
            fix_responses, error_msg = self.exchanges[exchange_name].request(msg)

            for fix_response in fix_responses:
                self.assert_msgtype(fix_response, Fix.Tags.MsgType.Values.EXECUTIONREPORT)
                found_orders = [x for x in open_orders.values() \
                                if x.OrderID.value == fix_response.OrderID.value]
                if len(found_orders) == 0:
                    # Not owned by the strategy
                    pass
                elif len(found_orders) == 1:
                    # Owned by the strategy
                    found_order = found_orders[0]
                    found_order.CumQty.value = fix_response.CumQty.value
                    found_order.LeavesQty.value = fix_response.LeavesQty.value
                    found_order.OrdStatus.value = fix_response.OrdStatus.value
                    found_order.ExecType.value = fix_response.ExecType.value
                    found_order.ExecID.value = self.get_next_exec_id()
                    update_fixtime(found_order, Fix.Tags.SendingTime.Tag)
                    self.insert_response_database(found_order)
                else:
                    assert False, "Unexpected more than 1 order is found."
            # OrdSvr handles it. No output
            return None
        else:
            assert False, "Not implemented MsgType %s" % msg.MsgType

    def __prepare_execution_report(self, msg, order_id, exec_id):
        """
        Prepare execution report
        """
        ret = Fix.Messages.ExecutionReport()
        update_fixtime(ret, Fix.Tags.SendingTime.Tag)

        ret.SecondaryClOrdID.value = order_id
        ret.ExecID.value = exec_id
        ret.Instrument.SecurityExchange.value = msg.Instrument.SecurityExchange.value
        ret.Instrument.Symbol.value = msg.Instrument.Symbol.value
        ret.Price.value = msg.Price.value
        ret.Side.value = msg.Side.value
        ret.OrderQtyData.OrderQty.value = msg.OrderQtyData.OrderQty.value
        ret.ClOrdID.value = msg.ClOrdID.value
        ret.OrdStatus.value = Fix.Tags.OrdStatus.Values.PENDING_NEW
        ret.ExecType.value = Fix.Tags.ExecType.Values.PENDING_NEW
        ret.CumQty.value = 0
        ret.LeavesQty.value = msg.OrderQtyData.OrderQty.value

        update_fixtime(ret, Fix.Tags.SendingTime.Tag)
        return ret

    def __handle_position_report(self, response):
        self.assert_msgtype(response, Fix.Tags.MsgType.Values.POSITIONREPORT)

        exchange_name = response.Instrument.SecurityExchange.value
        self.assert_exchange(exchange_name)

        exchange_exposure = self.exchange_risk_exposure[exchange_name]

        for group in response.PositionAmountData.groups:
            assert isinstance(group, Fix.Components.PositionAmountData.NoPosAmt)
            currency = group.PositionCurrency.value
            if group.PosAmtType.value == Fix.Tags.PosAmtType.Values.CASH_AMOUNT:
                exchange_exposure["Balance"][currency] = group.PosAmt.value
            elif group.PosAmtType.value == Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT:
                exchange_exposure["AvailableBalance"][currency] = group.PosAmt.value

