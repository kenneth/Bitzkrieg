#!/usr/bin/python3  
from bitz.id_generator import IdGenerator
import unittest

class TestIdGenerator(unittest.TestCase):
    def test_get_id(self):
        id_generator = IdGenerator()
        for i in range(0, 200):
            self.assertEqual("%s%02d" % (id_generator.prefix_id, i % 100), 
                             id_generator.get_id())
        
if __name__ == '__main__':
    unittest.main()