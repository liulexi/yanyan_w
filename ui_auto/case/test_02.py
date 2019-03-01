import unittest

class IntegerArithmeticTestCase(unittest.TestCase):
        # noinspection PyStatementEffect
        def setUp(self):
            print("打开浏览器")
        def tearDown(self):
            print("关闭浏览器")
        def testAdd(self):  # test method names begin with 'test'
            ''' 用例说明：加法案例 '''
            self.assertEqual((1 + 2), 3) # 断言失败显示截图
            self.assertEqual(0 + 1, 1) # 断言失败显示截图
            print("1111")
        def testMultiply(self):
            ''' 用例说明：乘法案例 '''
            self.assertEqual((0 * 10), 1) # 断言失败显示截图
            self.assertEqual((5 * 8), 2) # 断言失败显示截图
            print("2222")

if __name__ == '__main__':
    unittest.main()
