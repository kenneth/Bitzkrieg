#!/bin/python
from datetime import datetime
import os
import json


class AbstractJournalDatabase(object):
    """
    Abstract journal database
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    def connect(self, **kwargs):
        """
        Connect
        :param kwargs: Arguments
        """
        raise NotImplementedError()

    def insert(self, key, value):
        """
        Insert the key value pair
        :param key: Key
        :param value: Value
        """
        raise NotImplementedError()

    def get(self, key):
        """
        Get the key value pair
        :param key: Key
        :return: Value. None if not found.
        """
        raise NotImplementedError()


class InternalJournalDatabase(AbstractJournalDatabase):
    """
    In memory journal database
    """
    def __init__(self):
        """
        Constructor
        """
        self.__journal = {}
        self.__output_path = ''

    def __del__(self):
        """
        Destructor
        :return:
        """
        if self.__output_path != '':
            datetime_handler = lambda obj: obj.isoformat() if hasattr(obj, 'isoformat') else obj
            name = os.path.join(self.__output_path, 'journal_db_%s.db' % datetime.utcnow().strftime('%Y%m%d%H%M%S'))
            file = open(name, 'w+')
            file.write(json.dumps(self.__journal, indent=2, default=datetime_handler))
            file.close()

    def connect(self, **kwargs):
        """
        Connect
        :param kwargs: Arguments
        """
        self.__output_path = kwargs.setdefault('path', '')
        if not os.path.isdir(self.__output_path):
            prev_path = self.__output_path
            self.__output_path = ''
            assert False, "Invalid output path (%s)" % prev_path

    def insert(self, key, value):
        """
        Insert the key value pair
        :param key: Key
        :param value: Value
        """
        assert key not in self.__journal.keys(), "Duplicated key %s" % key
        self.__journal[key] = value
        return True

    def get(self, key):
        """
        Get the key value pair
        :param key: Key
        :return: Value. None if not found.
        """
        if key in self.__journal.keys():
            return self.__journal[key]
        else:
            return None

