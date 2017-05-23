#!/bin/python
from bitz.sql_client import SqlClient
from bitz.db_records import ActiveOrders
import unittest

class TClassSqlClient(SqlClient):
    """
    Test sql client
    """
    @classmethod
    def sql_convertor(cls, type):
        if type == int:
            return 'int'
        elif type == float:
            return 'float'
        elif type == str:
            return 'str'
        else:
            raise NotImplementedError('Type (%s) has not been defined yet.' % type)

    def __init__(self):
        """
        Constructor
        """
        SqlClient.__init__(self)
        self.committed_sql = []

    def execute(self, sql):
        """
        Execute
        :param sql: SQL
        :return: Always True
        """
        self.committed_sql.append(sql)
        return True

class TSqlClient(unittest.TestCase):
    """
    Sql client test case
    """
    def test_create_statement(self):
        """
        Test create statement
        """
        sql_client = TClassSqlClient()
        sql_client.create(ActiveOrders)
        self.assertEqual(1, len(sql_client.committed_sql))

    def test_insert_statement(self):
        """
        Test insert statement
        """
        sql_client = TClassSqlClient()
        sql_client.insert(ActiveOrders(date_time="20170519T18:00:00.000000"))
        self.assertEqual(1, len(sql_client.committed_sql))


if __name__ == '__main__':
    unittest.main()
