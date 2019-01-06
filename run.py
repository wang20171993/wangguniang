import unittest
from utils import HTMLTestRunner
import time
from utils import common

suite = unittest.defaultTestLoader.discover(start_dir='./cases',pattern='test*.py')
reportname = time.strftime('%Y-%m-%d-%H-%M-%S-')

with open("./reports/%s测试报告.html" % reportname,"wb") as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2,title='测试报告',description='执行人：浪晋')
    runner.run(suite)

