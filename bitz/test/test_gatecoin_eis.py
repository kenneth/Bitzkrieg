#!/usr/bin/python3  
from bitz.exch_gatecoin_eis import ExchGatecoinEis
from bitz.exch_gatecoin_eig import ExchGatecoinEig
from bitz.FIX50SP2 import FIX50SP2 as Fix
from bitz.logger import ConsoleLogger
from lightmatchingengine.lightmatchingengine import LightMatchingEngine, Side
from time import gmtime
import unittest

class TClassExchGatecoinEig(ExchGatecoinEig):
    def __init__(self,
                 logger,
                 key,
                 secret,
                 api_url = "https://api.gatecoin.com/"):
        ExchGatecoinEig.__init__(self, logger, key, secret, api_url)
        self.matching_engine = LightMatchingEngine()
        self.last_instmt = ""
    
    def generate_all_orders(self):
        orders = []
        for instmt, orderbook in self.matching_engine.order_books.items():
            for order_id, order in orderbook.order_id_map.items():
                if order.leaves_qty > 0:
                    side = 0 if order.side == Side.BUY else 1
                    price = order.price
                    initialQuantity = order.qty
                    remainingQuantity = order.leaves_qty
                    tranSeqNo = 0
                    if price > 0:
                        type = 0 # Limit
                    else:
                        type = 1 # Market
                    date = gmtime()
                        
                    if order.cum_qty > 0:
                        status = 2
                        statusDesc = "Filling"
                    else:
                        status = 1
                        statusDesc = "New"                        
                        
                    ret = { "code" : instmt,
                            "clOrderId" : order_id,
                            "side": side,
                            "price": price,
                            "initialQuantity": initialQuantity,
                            "remainingQuantity": remainingQuantity,
                            "tranSeqNo": tranSeqNo,
                            "type": type,
                            "date": date }
                    orders.append(ret)
        
        return orders
    
    def send_request(self, command, httpMethod, params={}):
        if command == "Trade/Orders" and httpMethod == "POST":
            # Place orders
            for key in ["Code", "Way", "Amount", "Price"]:
                assert key in params.keys(), \
                    "Key %s is not found in %s/%s" % (key, httpMethod, command)
            instmt = params["Code"]
            self.last_instmt = instmt
            price = params["Price"]
            qty = params["Amount"]
            side = Side.BUY if params["Way"] == "Bid" else Side.SELL
            order, _ = self.matching_engine.add_order(instmt, price, qty, side)
            ret = { "clOrderId" : "%d" % order.order_id, 
                     "responseStatus" : { "message" : "OK" } }
            return ret
        elif command == "Trade/Orders" and httpMethod == "DELETE":
            # Delete orders
            for key in ["clOrderId"]:
                assert key in params.keys(), \
                    "Key %s is not found in %s/%s" % (key, httpMethod, command)
            order_id = int(params["clOrderId"])
            order = self.matching_engine.cancel_order(order_id, self.last_instmt)   
            if order is not None:
                ret = { "responseStatus" : { "message" : "OK" } }
            else:
                ret = { "responseStatus" : { "message" : "Failed" } }
                
            return ret
        elif command == "Trade/Orders" and httpMethod == "GET":
            # Get order status
            orders = self.generate_all_orders()
            if "orderID" in params.keys():
                orders = [e for e in orders if params["orderID"] == e["clOrderId"]]
            
            ret = { "orders": orders }
            return ret
        else:
            assert False, "No implemented %s/%s" % (httpMethod, command)

class TestExchGatecoinEis(unittest.TestCase):
    def send_and_check_order(self, eis, symbol, side, price, qty):
        """
        Send and check the order
        :param eis              Exchange interface server
        :param symbol           Symbol
        :param side             Side
        :parma price            Price
        :param qty              Quantity
        :return Order id
        """
        req = Fix.Messages.NewOrderSingle()
        req.ClOrdID.value = "%s/%s/%.6f/%.6f" % (symbol, side, price, qty)
        req.Instrument.Symbol.value = symbol
        req.Side.value = side
        req.Price.value = price
        req.OrderQtyData.OrderQty.value = qty
        responses, err_msg = eis.request(req)
        self.assertEqual(1, len(responses))
        self.assertEqual("", err_msg)
        response = responses[0]
        self.assertEqual(Fix.Tags.MsgType.Values.EXECUTIONREPORT, response.MsgType)
        self.assertEqual(Fix.Tags.ExecType.Values.NEW, response.ExecType.value)
        self.assertEqual(Fix.Tags.OrdStatus.Values.NEW, response.OrdStatus.value)
        return response.OrderID.value
        
    def cancel_and_check_order(self, eis, order_id):
        req = Fix.Messages.OrderCancelRequest()
        req.OrderID.value = order_id
        responses, err_msg = eis.request(req)
        self.assertEqual(1, len(responses))
        self.assertEqual("", err_msg)
        response = responses[0]
        self.assertEqual(Fix.Tags.MsgType.Values.EXECUTIONREPORT, response.MsgType)
        self.assertEqual(Fix.Tags.ExecType.Values.CANCELED, response.ExecType.value)
        self.assertEqual(Fix.Tags.OrdStatus.Values.CANCELED, response.OrdStatus.value)        
    
    def test_request_order_single(self):
        eig = TClassExchGatecoinEig(ConsoleLogger.static_logger, "key", "secret")
        eis = ExchGatecoinEis(eig)
        # Send an order
        buy_order = self.send_and_check_order(eis, 
                                              "BTCUSD",
                                              Fix.Tags.Side.Values.BUY,
                                              1000.0,
                                              1.0)

    def test_request_order_cancel_request(self):
        eig = TClassExchGatecoinEig(ConsoleLogger.static_logger, "key", "secret")
        eis = ExchGatecoinEis(eig)
        
        # Send an order
        buy_order = self.send_and_check_order(eis, 
                                              "BTCUSD",
                                              Fix.Tags.Side.Values.BUY,
                                              1000.0,
                                              1.0)
        # Cancel the order
        self.cancel_and_check_order(eis, buy_order)
    
    def test_mass_order_request(self):
        eig = TClassExchGatecoinEig(ConsoleLogger.static_logger, "key", "secret")
        eis = ExchGatecoinEis(eig)
        # Send an order
        buy_order = self.send_and_check_order(eis, 
                                              "BTCUSD",
                                              Fix.Tags.Side.Values.BUY,
                                              1000.0,
                                              1.0)
        

if __name__ == '__main__':
    unittest.main()