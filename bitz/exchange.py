#!/bin/python
class Exchange(object):
    """
    Exchange
    """
    def __init__(self, name):
        """
        COnstructor
        """
        self.__name = name

    def get_name(self):
        """
        Get the exchange name
        """
        return self.__name

    def request(self, req):
        """
        Handle a request
        :param req              FIX message
        :return True if the request is successful.
        """
        return None, None

    def snapshot_updated(self, snapshot):
        """
        Snapshot updated
        :param snapshot: The instrument snapshot
        :return FIX message responses if provided.
        """
        pass
