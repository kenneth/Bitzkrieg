#!/bin/python
from bitz.journal_database import InternalJournalDatabase
from uuid import uuid4 as uuid
import unittest
import os
import glob

class TInternalJournalDatabase(unittest.TestCase):
    """
    InternalJournalDatabase test cases
    """
    @classmethod
    def tearDownClass(cls):
        """
        Tear down class
        """
        file_list = glob.glob(os.path.join('bitz', 'test', 'journal_db_*.db'))
        assert len(file_list) > 0, "Database file should be created."
        for file in file_list:
            os.remove(file)

    def test_create_and_insert(self):
        db = InternalJournalDatabase()
        db.connect(path=os.path.join('bitz', 'test'))
        db.insert(str(uuid()), str(uuid()))
        db.insert(str(uuid()), str(uuid()))
        db.insert(str(uuid()), str(uuid()))

    def test_connect_fail(self):
        db = InternalJournalDatabase()
        with self.assertRaises(AssertionError) as context:
            db.connect(path=os.path.join('WrongFolder', 'totalwrong', 'dumbfolder'))

if __name__ == '__main__':
    unittest.main()
