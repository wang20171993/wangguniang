import unittest
from utils import common

class TestExcle(unittest.TestCase):

    def test_01(self):
        a = common.getExcleValue('Sheet1',0,0)
        b = common.getExcleValue('Sheet1',0,1)
        c = common.getExcleValue('Sheet1',0,2)
        self.assertEqual(a*b,c)
        
