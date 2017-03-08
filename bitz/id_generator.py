#!/usr/bin/python3
from threading import Lock
from datetime import datetime

class IdGenerator:
    """
    Id generator. 
    """
    def __init__(self):
        """
        Constructor
        """
        self.prefix_id = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
        self.suffix_id = 0
        self.suffix_id_lock = Lock()
    
    def get_id(self):
        """
        Get id
        :return Id with the timestamp (YYYYmmddHHMMSSffffff) at the front
                and the suffix id at the end
        """
        # self.suffix_id_lock.acquire()
        ret = "%s%02d" % (self.prefix_id, self.suffix_id)
        self.suffix_id += 1
        if self.suffix_id >= 100:
            self.prefix_id = datetime.utcnow().strftime("%Y%m%d%H%M%S%f")
            self.suffix_id = 0
        # self.suffix_id_lock.release()
        
        return ret