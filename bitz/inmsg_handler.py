#!/usr/bin/python3 
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.FIX50SP2 import Tag, Component, RepeatingGroup, Message
import json

class InMsgHandler:
    """
    Incoming message handler
    """
    def __init__(self, logger, ordsvr):
        """
        Constructor
        """
        self.logger = logger
        self.ordsvr = ordsvr
        
    def handle(self, response):
        if response.MsgType == Fix.Tags.MsgType.Values.POSITIONREPORT:
            self.__handle_position_report(response)
        else:
            assert False, "Not yet implemented"
    
    def __handle_position_report(self, response):
        assert response.MsgType == Fix.Tags.MsgType.Values.POSITIONREPORT, \
            "Invalid msg type %s" % response.MsgType
            
        balances = self.ordsvr.balances
        available_balances = self.ordsvr.available_balances
        exchange = response.Instrument.SecurityExchange.value
        
        for group in response.PositionAmountData.groups:
            assert isinstance(group, Fix.Components.PositionAmountData.NoPosAmt)
            currency = group.PositionCurrency.value
            if group.PosAmtType.value == Fix.Tags.PosAmtType.Values.CASH_AMOUNT:
                balances[(exchange, currency)] = group.PosAmt.value
            elif group.PosAmtType.value == Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT:
                available_balances[(exchange, currency)] = group.PosAmt.value                
        
        balances_str = ''
        available_balances_str = ''
        for key, value in balances.items():
            balances_str += '%s,%s: %.6f\n' % (key[0], key[1], balances[key])
            available_balances_str += '%s,%s: %.6f\n' % (key[0], key[1], available_balances[key])
            
        self.logger.info(self.__class__.__name__, "Updated balance summary:\n%s" % balances_str)
        self.logger.info(self.__class__.__name__, "Updated available balance summary:\n%s" % available_balances_str)
    
    @staticmethod
    def to_dict(input):
        if isinstance(input, RepeatingGroup):
            ret = []
            for group in input.groups:
                ret.append(InMsgHandler.to_dict(group))
                
            return ret
        elif isinstance(input, Message) or isinstance(input, Component):
            ret = {}
            for name, attr in input.__dict__.items():
                ret[name] = InMsgHandler.to_dict(attr)
                
            return ret
        elif isinstance(input, Tag):
            return input.value
        elif isinstance(input, bool):
            pass
        else:
            assert False, "Unknow type %s" % input.__class__.__name__