import unittest
from utils import pyselenium
from utils import common
import time



class Testbaidu(unittest.TestCase):
    '''
    测试用例
    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = pyselenium.Pyselenium('Chrome')
        cls.driver.open('http://www.baidu.com')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_01_text(self):
        '''
        测试用例1
        '''
        time.sleep(3)
        self.driver.send('id->kw','浪晋的测试小讲堂')
        time.sleep(3)
        self.driver.click('id->su')
        title = self.driver.gettitle()
        jieguo = common.getExcleValue('Sheet1',1,0)
        # sql = 'select classname from class where id = 3'
        # jieguo  = common.getDbValue(sql)[0][0]
        self.assertEqual(title,jieguo)


    # def test_02_text(self):
    #     '''
    #     测试用例2
    #     '''
    #     neirong = self.driver.find_element_by_xpath("//*[@id=\"section-rule\"]/h2").text
    #     self.assertEqual(neirong,'使用规则')
        

