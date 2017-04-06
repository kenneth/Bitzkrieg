#!/usr/bin/python3  
from bitz.redis_database_client import RedisDatabaseClient
import unittest
from unittest.mock import patch, MagicMock


class TestRedisDatabaseClient(unittest.TestCase):
    @patch('bitz.redis_database_client.redis.StrictRedis')
    def test_insert(self, mock_strictredis):
        client = RedisDatabaseClient()
        client.connect(host='localhost', 
                       port=9999,
                       db=3)
        client.db_client.set.return_value = True
        self.assertTrue(client.insert('key1', 1))
        client.db_client.set.assert_called_with('key1', 1)

if __name__ == '__main__':
    unittest.main()
