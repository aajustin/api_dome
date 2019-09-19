import unittest
from BeautifulReport import BeautifulReport
import time

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_suite = unittest.defaultTestLoader.discover('./api_test', pattern='test_*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='接口自动化测试报告' + now, description='订单流程接口测试', log_path='report')
