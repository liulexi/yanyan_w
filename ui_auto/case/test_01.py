from selenium import webdriver
import time
import unittest
class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://www.juhe.cn/login?ref=https://www.juhe.cn/account")
    def tearDown(self):
        self.driver.quit()
    def login(self,user,pwd):
        self.driver.find_element_by_id("username").send_keys(user)
        self.driver.find_element_by_id("password").send_keys(pwd)
        self.driver.find_element_by_id("loginBtn").click()
    def test_001(self):
        ''' 用例说明：登录成功案例 '''
        self.login("oishi999","Ly19910520..")
        time.sleep(3)
        # 判断是否登录成功
        t=self.driver.title
        print(t)
        self.assertTrue(t=="聚合数据个人中心") # 断言失败显示截图

    def test_002(self):
        ''' 用例说明：登录失败案例 '''
        self.login("oishi9","Ly19910520..")
        time.sleep(3)
        # 判断是否登录成功
        t=self.driver.title
        print(t)
        self.assertTrue(t=="聚合数据个人中心") # 断言失败显示截图
if __name__ == "__main__":
    unittest.main()
help(unittest)


