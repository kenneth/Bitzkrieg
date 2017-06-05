#!/bin/python
class Exchange(object):
    """
    Exchange
    """
    def __init__(self):
        """
        COnstructor
        """
        pass

    @classmethod
    def get_name(cls):
        """
        Get the exchange name
        """
        raise NotImplementedError("Not yet implemented get_name.")

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
