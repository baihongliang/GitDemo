import unittest

from util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    # 方法四：discover
    test_dir = "./test_pytest"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    # unittest.TextTestRunner(verbosity=2).run(discover)

    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)