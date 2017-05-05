#!/bin/python
from bitz.realtime_database import InternalRealtimeDatabase
from bitz.FIX50SP2 import FIX50SP2 as Fix
from uuid import uuid4 as uuid
import unittest
import os
import glob

class TInternalRealtimeDatabase(unittest.TestCase):
    """
    InternalRealtimeDatabase test cases
    """
    @classmethod
    def tearDownClass(cls):
        """
        Tear down class
        """
        file_list = glob.glob(os.path.join('bitz', 'test', 'historical_requests_*.db'))
        assert len(file_list) > 0, "Database file should be created."
        for file in file_list:
            os.remove(file)

        file_list = glob.glob(os.path.join('bitz', 'test', 'execution_report_cache_*.db'))
        assert len(file_list) > 0, "Database file should be created."
        for file in file_list:
            os.remove(file)

    def test_create_and_insert(self):
        db = InternalRealtimeDatabase()
        db.connect(path=os.path.join('bitz', 'test'))
        # Initialize the request
        request = Fix.Messages.NewOrderSingle()
        request.Instrument.Symbol.value = 'BTC'
        request.Instrument.SecurityExchange.value = 'Exchange'
        request.ClOrdID.value = str(uuid)
        # Initialize the response
        response = Fix.Messages.ExecutionReport()
        response.Instrument.Symbol.value = request.Instrument.Symbol.value
        response.Instrument.SecurityExchange.value = request.Instrument.SecurityExchange.value
        response.ClOrdID.value = request.ClOrdID.value
        response.ExecType.value = Fix.Tags.ExecType.Values.NEW
        response.OrderID.value = str(uuid())
        # Update the database
        db.update(request, response)

    def test_connect_fail(self):
        db = InternalRealtimeDatabase()
        with self.assertRaises(AssertionError) as context:
            db.connect(path=os.path.join('WrongFolder', 'totalwrong', 'dumbfolder'))

if __name__ == '__main__':
    unittest.main()
