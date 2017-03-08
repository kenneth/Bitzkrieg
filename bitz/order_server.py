#!/usr/bin/python3 
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.util import update_sendingtime, fixmsg2dict
from datetime import datetime

class OrderServer:
    """
    Order server
    
    The server maintains the following:
    1. House order book
    2. Risk level and limit
    3. Exchange interface
    4. Archive all the incoming and outgoing messages
    
    All the communication is via FIX protocol.
    """
    def __init__(self, request_database, response_database, logger):
        """
        Constructor
        """
        self.request_database = request_database
        self.response_database = response_database
        self.logger = logger
        self.exchanges = {}
        self.active_orders = {}
        self.exchange_risk_exposure = {}
        self.strategy_risk_exposure = {}
        self.current_order_id = int(datetime.utcnow().strftime("%Y%m%d%H%M%S")) * 100
        self.current_exec_id = 0
    
    def get_next_order_id(self):
        self.current_order_id += 1
        return self.current_order_id
        
    def get_next_exec_id(self):
        self.current_exec_id += 1
        return self.current_exec_id
    
    def register_gateway(self, exchange_name, exchange_server):
        """
        Register a gateway
        """
        assert exchange_name not in self.exchanges.keys(), \
               "Duplicated registeration of exchange %s" % exchange_name
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
        assert strategy not in self.strategy_risk_exposure.keys(), \
               "Duplicated strategy %s" % strategy.get_name()
        self.strategy_risk_exposure[strategy] = {}
        
    def query_risk_exposure(self):
        """
        Query the risk exposure among all exchanges and strategies
        """
        for name, exchange in self.exchanges.items():
            req = Fix.Messages.RequestForPositions()
            update_sendingtime(req)
            req.PosReqID.value = self.get_next_order_id()
            req.Instrument.SecurityExchange.value = name
            self.request(self, req)
        
    def request(self, source, msg):
        """
        Request
        """
        exchange = msg.Instrument.SecurityExchange.value
        assert exchange in self.exchanges.keys(), \
               "Exchange %s has not been registered yet." % exchange
        
        if msg.MsgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            # Handle add order
            
            # Add risk level
            if msg.Side.value == Fix.Tags.Side.Values.BUY:
                self.strategy_risk_exposure[source]['open_bid_amt'] += msg.OrderQtyData.OrderQty.value
            elif msg.Side.value == Fix.Tags.Side.Values.SELL:
                self.strategy_risk_exposure[source]['open_ask_amt'] += msg.OrderQtyData.OrderQty.value
            else:
                assert False, "Invalid Side %s" % msg.Side.value
            
            # Add latency trip
            update_sendingtime(msg, "OrdSvr")
            
            # Prepare the execution report
            ordsvr_response = self.__prepare_execution_report(msg, self.get_next_order_id(), self.get_next_exec_id())
            
            # Store request into the database
            self.request_database.insert(ordsvr_response.OrderID.value, fixmsg2dict(msg))
            
            # Send it to the exchange
            gw_responses, error_msg = self.exchanges[exchange].request(msg)
            for gw_response in gw_responses:
                if gw_response.ExecType.value == Fix.Tags.ExecType.Values.NEW:
                    ordsvr_response.ExecType.value = Fix.Tags.ExecType.Values.NEW
                    ordsvr_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.NEW
                    ordsvr_response.SecondaryOrderID.value = gw_response.OrderID.value
                elif gw_response.ExecType.value == Fix.Tags.ExecType.Values.REJECTED:
                    ordsvr_response.OrdStatus.value = Fix.Tags.OrdStatus.Values.REJECTED
                    ordsvr_response.ExecType.value = Fix.Tags.ExecType.Values.REJECTED
                    ordsvr_response.Text.value = gw_response.Text
                else:
                    assert False, "Not implemented other ExecType %s" % gw_response.ExecType.value
            
            # Add latency trip
            update_sendingtime(ordsvr_response, "OrdSvr")
            
            # Store response into the database
            self.response_database.insert("%s-%05d" % (ordsvr_response.OrderID.value, ordsvr_response.ExecID.value),
                                          fixmsg2dict(ordsvr_response))
            return ordsvr_response
            
        elif msg.MsgType == Fix.Tags.MsgType.Values.REQUESTFORPOSITIONS:
            # Handle request for positions
            
            # Add latency trip
            update_sendingtime(msg, "OrdSvr")
            
            # Store request into the database
            self.request_database.insert(msg.PosReqID.value, fixmsg2dict(msg))            
            
            gw_responses, error = self.exchanges[exchange].request(msg)
            for gw_response in gw_responses:
                if gw_response.MsgType == Fix.Tags.MsgType.Values.POSITIONREPORT:
                    gw_response.PosMaintRptID.value = self.get_next_exec_id()
                    gw_response.PosReqID.value = msg.PosReqID.value
                    update_sendingtime(gw_response, "OrdSvr")
                    self.response_database.insert("%s-%05d" % \
                        (gw_response.PosReqID.value, gw_response.PosMaintRptID.value), \
                         fixmsg2dict(gw_response))                    
                    self.__handle_position_report(gw_response)
                else:
                    assert False, "Expected to allow only POSITIONREPORT." + \
                                  ("MsgType: %s" % gw_response.MsgType) 
            
            # OrdSvr handles it. No output
            return None
        else:
            assert False, "Not implemented MsgType %s" % msg.MsgType
            
    def __prepare_execution_report(self, msg, order_id, exec_id):
        """
        Prepare execution report
        """
        ret = Fix.Messages.ExecutionReport()
        update_sendingtime(ret)
        ret.OrderID.value = order_id
        ret.ExecID.value = exec_id
        ret.Instrument.SecurityExchange.value = msg.Instrument.SecurityExchange.value
        ret.Instrument.Symbol.value = msg.Instrument.Symbol.value
        ret.Price.value = msg.Price.value
        ret.Side.value = msg.Side.value
        ret.OrderQtyData.OrderQty.value = msg.OrderQtyData.OrderQty.value
        ret.ClOrdID.value = msg.ClOrdID.value
        ret.OrdStatus.value = Fix.Tags.OrdStatus.Values.PENDING_NEW
        ret.ExecType.value = Fix.Tags.ExecType.Values.PENDING_NEW
        update_sendingtime(ret)
        return ret
        
    def __handle_position_report(self, response):
        assert response.MsgType == Fix.Tags.MsgType.Values.POSITIONREPORT, \
            "Invalid msg type %s" % response.MsgType
            
        exchange = response.Instrument.SecurityExchange.value
        
        assert exchange in self.exchange_risk_exposure.keys(), \
               "Exchange %s has not been registered yet." % exchange
               
        exchange_exposure = self.exchange_risk_exposure[exchange]
        
        for group in response.PositionAmountData.groups:
            assert isinstance(group, Fix.Components.PositionAmountData.NoPosAmt)
            currency = group.PositionCurrency.value
            if group.PosAmtType.value == Fix.Tags.PosAmtType.Values.CASH_AMOUNT:
                exchange_exposure["Balance"][currency] = group.PosAmt.value
            elif group.PosAmtType.value == Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT:
                exchange_exposure["AvailableBalance"][currency] = group.PosAmt.value                
                