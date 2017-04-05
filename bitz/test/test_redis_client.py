#!/usr/bin/python3  
import redis
from bitz.redis_database_client import RedisDatabaseClient
import mock
import unittest

class TestRedisDatabaseClient(unittest.TestCase):
    
    @mock.patch.object(redis.StrictRedis, 'set', autospec=True)
    def test_insert(self, mock_strictredis):
        client = RedisDatabaseClient()
        client.connect(host='localhost', 
                       port=9999,
                       db=3)
        client.insert('key1', 1)
        mock_strictredis.assert_called_with(name='key1', value=1)
        # self.assertTrue(client.insert('key2', 2))
        
if __name__ == '__main__':
    unittest.main()
