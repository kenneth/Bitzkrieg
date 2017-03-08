#!/usr/bin/python3  
import redis
import json

class RedisDatabaseClient:
    """
    Redis database client
    """
    def __init__(self):
        """
        Constructor
        """
        self.db_client = None
        
    def connect(self, **kargs):
        """
        Connect
        """
        host = kargs['host']
        port = kargs['port']
        db = kargs['db'] if 'db' in kargs else 0
        
        self.db_client = redis.StrictRedis(host=host, port=port, db=db)
    
    def insert(self, key, obj):
        """
        Insert
        """        
        return self.db_client.set(key, obj)
        