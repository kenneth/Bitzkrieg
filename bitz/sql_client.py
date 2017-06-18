#!/bin/python
from bitz.db_records import TableRecord
import threading
import sqlite3
import pymysql

class SqlClient:
    """
    Sql client
    """
    @classmethod
    def convert_type(cls, type):
        if type == int:
            return 'int'
        elif type == float:
            return 'decimal(20,8)'
        elif type == str:
            return 'varchar(25)'
        else:
            raise NotImplementedError('Type (%s) has not been defined yet.' % type)

    @classmethod
    def get_auto_increment_keyword(cls):
        return ""

    def __init__(self):
        """
        Constructor
        """
        self.conn = None
        self.cursor = None
        self.lock = threading.Lock()

    def connect(self, **kwargs):
        """
        Connect
        """
        raise NotImplementedError("Method not yet implemented.")

    def execute(self, sql):
        """
        Execute the sql command
        :param sql: SQL command
        """
        return True

    def commit(self):
        """
        Commit
        """
        return True

    def fetchone(self):
        """
        Fetch one record
        :return Record
        """
        return []

    def fetchall(self):
        """
        Fetch all records
        :return Record
        """
        return []

    def close(self):
        """
        Close
        :return:
        """
        pass

    def create(self, record: TableRecord):
        """
        Create table in the database
        :param record: Record
        """
        self.lock.acquire()
        sql = ""

        try:
            sql = record.create_sql_stmt(self)
            self.execute(sql)
        except Exception as e:
            raise Exception("Error in create statement (%s).\nError: %s\n" % (sql, e))

        self.commit()
        self.lock.release()

        return True

    def insert(self, record: TableRecord):
        """
        Insert into the table
        """
        self.lock.acquire()
        sql = ""

        try:
            if 'id' not in record.values.keys():
                id = TableRecord.Id
                TableRecord.Id += 1
                record.values['id'] = id

            sql = record.insert_sql_stmt()
            self.execute(sql)
        except Exception as e:
            raise Exception("Error in insert statement (%s).\nError: %s\n" % (sql, e))

        self.commit()
        self.lock.release()

    def select(self, record: TableRecord, condition='', orderby='', limit=0, isFetchAll=True):
        """
        Select rows from the table
        :return Result rows
        """
        self.lock.acquire()

        if len(record.values) == 0:
            sql = "select * from %s " % record.name()
        else:
            sql = "select %s from %s " % (','.join(record.keys()), record.name())

        if condition != '':
            sql += "where %s " % condition

        if orderby != '':
            sql += "order by %s " % orderby

        if limit > 0:
            sql += "limit %d" % limit

        self.execute(sql)
        if isFetchAll:
            ret = self.fetchall()
        else:
            ret = self.fetchone()

        self.lock.release()
        return ret


class SqliteClient(SqlClient):
    """
    Sqlite client
    """
    def __init__(self):
        SqlClient.__init__(self)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    @classmethod
    def get_auto_increment_keyword(cls):
        return ""

    def connect(self, **kwargs):
        """
        Connect
        :return:
        """
        path = kwargs['path']
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        return self.conn is not None and self.cursor is not None

    def execute(self, sql):
        """
        Execute the sql command
        :param sql: SQL command
        """
        self.cursor.execute(sql)


    def commit(self):
        """
        Commit
        """
        self.conn.commit()


    def fetchone(self):
        """
        Fetch one record
        :return Record
        """
        return self.cursor.fetchone()


    def fetchall(self):
        """
        Fetch all records
        :return Record
        """
        return self.cursor.fetchall()

class MysqliteClient(SqlClient):
    """
    Sqlite client
    """
    def __init__(self):
        SqlClient.__init__(self)

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    @classmethod
    def convert_type(cls, type):
        if type == int:
            return 'bigint'
        elif type == float:
            return 'decimal(20,8)'
        elif type == str:
            return 'varchar(75)'
        else:
            raise NotImplementedError('Type (%s) has not been defined yet.' % type)

    @classmethod
    def get_auto_increment_keyword(cls):
        return "auto_increment"

    def connect(self, **kwargs):
        """
        Connect
        :return:
        """
        host = kwargs['host']
        port = kwargs['port']
        user = kwargs['user']
        pwd = kwargs['pwd']
        schema = kwargs['schema']
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=pwd,
                                    db=schema,
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()
        return self.conn is not None and self.cursor is not None

    def execute(self, sql):
        """
        Execute the sql command
        :param sql: SQL command
        """
        self.cursor.execute(sql)


    def commit(self):
        """
        Commit
        """
        self.conn.commit()


    def fetchone(self):
        """
        Fetch one record
        :return Record
        """
        return self.cursor.fetchone()


    def fetchall(self):
        """
        Fetch all records
        :return Record
        """
        return self.cursor.fetchall()
