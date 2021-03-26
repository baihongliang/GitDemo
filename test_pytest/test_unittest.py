import unittest


class TestStringMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self):
        print("teardown")

    def test_upper(self):
        print("1")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("2")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("3")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


# unittest不能执行单独的测试函数
def test_func():
    print(1111)
    pass


if __name__ == '__main__':
    # 方法一：执行当前文件所有的unittest测试用例
    # unittest.main()

    # 方法二：创建测试套件，执行指定的测试用例
    # suite = unittest.TestSuite()
    # suite.addTest(TestStringMethods("test_upper"))
    # suite.addTest(TestStringMethods("test_split"))
    # unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类或多个测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(suite)
