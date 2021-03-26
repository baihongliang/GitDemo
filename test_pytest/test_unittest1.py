import unittest

if __name__ == '__main__':
    # 方法四：discover
    test_dir = "../test_pytest"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    unittest.TextTestRunner(verbosity=2).run(discover)