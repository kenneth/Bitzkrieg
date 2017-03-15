#!/usr/bin/python3  
from bitz.redis_database_client import RedisDatabaseClient
from subprocess import Popen
import unittest
import time

class TestRedisDatabaseClient(unittest.TestCase):
    server = None
    server_port = 9999
    
    @classmethod
    def setUpClass(cls):
        server = Popen(["redis-server", "--port %d" % TestRedisDatabaseClient.server_port])
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        if TestRedisDatabaseClient.server is not None:
            TestRedisDatabaseClient.server.terminate()
    
    def test_insert(self):
        client = RedisDatabaseClient()
        client.connect(host='localhost', 
                       port=TestRedisDatabaseClient.server_port,
                       db=3)
        self.assertTrue(client.insert('key1', 1))
        self.assertTrue(client.insert('key2', 2))
        
if __name__ == '__main__':
    unittest.main()
