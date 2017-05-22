from bitz.realtime_database import SqliteRealtimeDatabase
from bitz.fix_message_factory import FixMessageFactory
from bitz.db_records import ActiveOrders
from bitz.db_records import Balances
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

    def test_create_and_insert_active_orders(self):
        db = SqliteRealtimeDatabase()
        db.connect(path=os.path.join('bitz',
                                     'test',
                                     'test_realtime_db_%s.db' % datetime.utcnow().strftime("%y%m%d%H%M%S%f")))
        req = FixMessageFactory.create_new_single_order(symbol='BTCUSD',
                                                        exchange='Gatecoin',
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

    def test_create_and_insert_balances(self):
        db = SqliteRealtimeDatabase()
        db.connect(path=os.path.join('bitz',
                                     'test',
                                     'test_realtime_db_%s.db' % datetime.utcnow().strftime("%y%m%d%H%M%S%f")))

        # Generate position report
        fix_message = Fix.Messages.PositionReport()
        fix_message.PosReqID.value = str(uuid())
        fix_message.Instrument.SecurityExchange.value = 'TestExchange'
        fix_message.ClearingBusinessDate.value = datetime.utcnow().strftime("%y%m%d%H%M%S%f")
        fix_message.PosMaintRptID.value = datetime.utcnow().strftime("%y%m%d%H%M%S%f") + str(uuid())

        for currency, total_balance, available_balance in \
                [('USD', 2000, 2000),
                 ('HKD', 100000, 100000),
                 ('BTC', 10, 10)]:
            # Total
            positionAmountData = Fix.Components.PositionAmountData.NoPosAmt()
            positionAmountData.PositionCurrency.value = currency
            positionAmountData.PosAmt.value = total_balance
            positionAmountData.PosAmtType.value = Fix.Tags.PosAmtType.Values.CASH_AMOUNT
            fix_message.PositionAmountData.groups.append(positionAmountData)

            # Available
            positionAmountData = Fix.Components.PositionAmountData.NoPosAmt()
            positionAmountData.PositionCurrency.value = currency
            positionAmountData.PosAmt.value = available_balance
            positionAmountData.PosAmtType.value = Fix.Tags.PosAmtType.Values.FINAL_MARK_TO_MARKET_AMOUNT
            fix_message.PositionAmountData.groups.append(positionAmountData)

        # Simply skip the position request message, as not used
        db.update(None, fix_message)

        # Get DB records and check
        records = db.get_database().select(Balances())
        self.assertEqual(3, len(records))

if __name__ == '__main__':
    unittest.main()
