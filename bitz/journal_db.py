#!/bin/python
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

    def connect(self, **kwargs):
        """
        Connect
        :param kwargs: Arguments
        """
        pass

    def insert(self, key, value):
        """
        Insert the key value pair
        :param key: Key
        :param value: Value
        """
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

