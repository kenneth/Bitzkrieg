#!/bin/python
class TableRecord(object):
    """
    Table record
    """
    Id = 1

    def __init__(self, **kwargs):
        self.values = kwargs

    @classmethod
    def name(cls):
        raise NotImplementedError('No table name is provided.')

    @classmethod
    def columns(cls):
        return []

    @classmethod
    def primary_keys(cls):
        return []

    @classmethod
    def create_sql_stmt(cls, sql_cls):
        """
        SQL statement on create
        :param convertor: Type convertor
        :return: Sql statement
        """
        sql = "create table if not exists %s (" % cls.name()
        for column in cls.columns():
            field = column[0]
            type = column[1]
            autoincrement = column[2] if len(column) > 2 else False

            if not autoincrement:
                sql += "%s %s," % (field, sql_cls.convert_type(type))
            else:
                sql += "%s %s %s," % (field, sql_cls.convert_type(type), sql_cls.get_auto_increment_keyword())

        if len(cls.primary_keys()) > 0:
            sql += "primary key (%s)" % (", ".join(cls.primary_keys()))
        else:
            sql = sql[0:len(sql) - 1]
        sql += ")"
        return sql

    def insert_sql_stmt(self):
        """
        SQL statement on insert
        :return: Sql statement
        """
        included_fields = ""
        included_values = ""
        for column in self.columns():
            field = column[0]
            type = column[1]
            autoincrement = column[2] if len(column) > 2 else False

            if field in self.values.keys() and not autoincrement:
                value = self.values[field]
                if value is not None:
                    if type == str:
                        included_values += ("\'" + str(value) + "\',")
                    else:
                        included_values += (str(value) + ",")
                    included_fields += (field + ",")
        included_fields = included_fields[0:len(included_fields)-1]
        included_values = included_values[0:len(included_values)-1]
        sql = "insert into %s (%s) values (%s)" % (self.name(), included_fields, included_values)
        return sql


class ActiveOrders(TableRecord):
    """
    Active order
    """
    @classmethod
    def name(cls):
        return 'ACTIVE_ORDERS'

    @classmethod
    def columns(cls):
        """
        Columns
                 FieldName            | FieldType | AutoIncrement
        """
        return [('id',                  int,        True),
                ('timestamp',           str),
                ('exchange',            str),
                ('instmt_name',         str),
                ('orderid',             str),
                ('side',                str),
                ('price',               float),
                ('orderqty',            float),
                ('cumqty',              float),
                ('leavesqty',           float),
                ('avgpx',               float),
                ('ordstatus',           str),
                ('exectype',            str),
                ('ordtype',             str),
                ('timeinforce',         str),
                ('clordid',             str),
                ('transacttime',        str)
                ]

    @classmethod
    def primary_keys(cls):
        return ['id']


class Balances(TableRecord):
    """
    Balances
    """

    @classmethod
    def name(cls):
        return 'BALANCES'

    @classmethod
    def columns(cls):
        """
        Columns
                 FieldName            | FieldType | AutoIncrement
        """
        return [('id',                  int,        True),
                ('timestamp',           str),
                ('exchange',            str),
                ('ccy',                 str),
                ('balance',             float),
                ('availableBalance',    float),
                ('account',             str)
                ]

    @classmethod
    def primary_keys(cls):
        return ['id']


class OrderRequests(TableRecord):
    @classmethod
    def name(cls):
        return 'ORDER_REQUESTS'

    @classmethod
    def columns(cls):
        """
        Columns
                 FieldName    | FieldType | AutoIncrement
        """
        return [('id',          int,        True),
                ('msgtype',     str),
                ('timestamp',   str),
                ('clordid',     str),
                ('exchange',    str),
                ('instmt_name', str),
                ('orderid',     str),
                ('side',        str),
                ('price',       float),
                ('orderqty',    float),
                ('ordtype',     str),
                ('timeinforce', str),
                ('sendingtime', str)
                ]

    @classmethod
    def primary_keys(cls):
        return ['id']
