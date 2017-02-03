#!/usr/bin/python3  
from bitz.util import RequestCode
from bitz.logger import Logger
from bitz.FIX50SP2 import FIX50SP2 as Fix

class ExchGatecoinEis(object):
    """
    Exchange gateway server
    """
    def __init__(self, eig):
        self.eig = eig
    
    def request(self, req):
        """
        Handle a request
        :param req              FIX message
        :return True if the request is successful.
        """
        assert Fix.Tags.MsgType.Tag in req.keys(), \
            "Cannot find MsgType in the message"
            
        msgType = req[Fix.Tags.MsgType.Tag]
        
        if msgType == Fix.Tags.MsgType.Values.NEWORDERSINGLE:
            response = self.request_order_single(req)
            
            if self.eig.check_success(response):
                return { 
                    Fix.Tags.MsgType.Tag: Fix.Tags.MsgType.Values.EXECUTIONREPORT,
                    Fix.Tags.OrderID.Tag: response['clOrderId'],
                    Fix.Tags.ExecType.Tag: Fix.Tags.ExecType.Values.NEW
                    }
            else:
                assert False, "Not yet implemented"
                
        elif msgType == Fix.Tags.MsgType.Values.ORDERCANCELREQUEST:
            pass
        else:
            assert False, "MsgType (%s) has not yet been implemented." % msgType
        
    def request_order_single(self, req):
        symbol = req[Fix.Tags.Symbol.Tag]
        price = req[Fix.Tags.Price.Tag]
        orderQty = req[Fix.Tags.OrderQty.Tag]
        side = req[Fix.Tags.Side.Tag]
        params = { "Code": symbol, 
                    "Way": 'Bid' if side == Fix.Tags.Side.Values.BUY else 'Ask',
                    "Amount": orderQty,
                    "Price": price
                }
        
        return self.eig.send_request("Trade/Orders", "POST", params)
        
    def request_order_cancel_request(self, req):
        assert False, "Not yet implemented."
        