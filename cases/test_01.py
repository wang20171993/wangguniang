import unittest
from selenium import webdriver

class TestDemo(unittest.TestCase):
    # def setUp(self):
    #     print("测试开始")

    # def tearDown(self):
    #     print("测试结束")

    @classmethod
    def setUpClass(cls):
        print("测试开始")

    @classmethod
    def tearDownClass(cls):
        print("\n测试结束")

    def test_01_add(self):
        self.assertEqual(1+1,2,"加法")

    def test_02_jian(self):
        self.assertEqual(1-1,0,"剪法")

    def test_03_cheng(self):
        self.assertEqual(1*1,1,"乘法")

    def test_04_chu(self):
        self.assertEqual(1/1,1,"除法")

