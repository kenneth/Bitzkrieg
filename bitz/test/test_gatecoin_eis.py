#!/usr/bin/python3  
from bitz.exch_gatecoin_eis import ExchGatecoinEis
from bitz.exch_gatecoin_eig import ExchGatecoinEig
from bitz.FIX50SP2 import FIX50SP2 as Fix
import unittest

class TClassExchGatecoinEig(ExchGatecoinEig):
    def send_request(self, command, httpMethod, params={}):
        if command == "Trade/Orders" and httpMethod == "POST":
            for key in ["Code", "Way", "Amount", "Price"]:
                assert key in params.keys(), \
                    "Key %s is not found in %s/%s" % (key, httpMethod, command)
            
            return { "clOrderId" : "Testing/%s/%s" % (httpMethod, command), 
                     "responseStatus" : { "message" : "OK" } }
        else:
            assert False, "No implemented %s/%s" % (httpMethod, command)

class TestExchGatecoinEis(unittest.TestCase):
    def test_request_order_single(self):
        eig = TClassExchGatecoinEig("key", "secret")
        eis = ExchGatecoinEis(eig)
        req = {}
        req[Fix.Tags.MsgType.Tag] = Fix.Tags.MsgType.Values.NEWORDERSINGLE
        req[Fix.Tags.ClOrdID.Tag] = "Teseting-Sending"
        req[Fix.Tags.Symbol.Tag] = "BTCUSD"
        req[Fix.Tags.Side.Tag] = Fix.Tags.Side.Values.BUY
        req[Fix.Tags.Price.Tag] = 1000.0
        req[Fix.Tags.OrderQty.Tag] = 1.0
        response = eis.request(req)
        self.assertEqual(Fix.Tags.MsgType.Values.EXECUTIONREPORT, response[Fix.Tags.MsgType.Tag])
        self.assertEqual(Fix.Tags.ExecType.Values.NEW, response[Fix.Tags.ExecType.Tag])
        self.assertEqual("Testing/POST/Trade/Orders", response[Fix.Tags.OrderID.Tag])

if __name__ == '__main__':
    unittest.main()