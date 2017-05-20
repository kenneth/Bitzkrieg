from bitz.realtime_database import SqliteRealtimeDatabase
from bitz.fix_message_factory import FixMessageFactory
from bitz.db_records import ActiveOrders
from bitz.FIX50SP2 import FIX50SP2 as Fix
from uuid import uuid4 as uuid
from datetime import datetime
import unittest
import os
import glob

class TSqliteRealtimeDatabase(unittest.TestCase):
    """
    Test case for sqlite realtime database
    """
    @classmethod
    def tearDownClass(cls):
        """
        Tear down class
        """
        file_list = glob.glob(os.path.join('bitz', 'test', 'test_realtime_db_*.db'))
        assert len(file_list) > 0, "Database file should be created."
        for file in file_list:
            os.remove(file)

    def test_create_and_insert(self):
        db = SqliteRealtimeDatabase()
        db.connect(path=os.path.join('bitz',
                                     'test',
                                     'test_realtime_db_%s.db' % datetime.utcnow().strftime("%y%m%d%H%M%S%f")))
        req = FixMessageFactory.create_new_single_order(symbol='Gatecoin',
                                                        exchange='BTCUSD',
                                                        clordid=str(uuid()),
                                                        price=2000,
                                                        qty=1,
                                                        side=Fix.Tags.Side.Values.BUY,
                                                        ordtype=Fix.Tags.OrdType.Values.LIMIT,
                                                        timeinforce=Fix.Tags.TimeInForce.Values.DAY,
                                                        transacttime=datetime.utcnow().strftime("%Y%m%dT%H:%M:%S.%f"))
        ack = FixMessageFactory.create_execution_report_from_new_order_single(req, orderid=str(uuid()))
        db.update(req, ack)
        records = db.get_database().select(ActiveOrders())
        self.assertEqual(1, len(records))
        ack.LastPx.value = ack.Price.value
        ack.LastQty.value = 0.1
        ack.CumQty.value = ack.LastQty.value
        ack.AvgPx.value = ack.Price.value
        db.update(req, ack)
        records = db.get_database().select(ActiveOrders())
        self.assertEqual(2, len(records))

if __name__ == '__main__':
    unittest.main()
