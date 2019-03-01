#coding:utf-8
import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner
casePath=r"F:\PycharmProjects\ui_auto\case"
rule="test*.py"
discover=unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
reportPath="F:\\PycharmProjects\\ui_auto\\report\\"+"result.html"
fp=open(reportPath,"wb")

if __name__ == '__main__':
 runner=HTMLTestRunner(stream=fp,
                   title="2019-2-14-test",
                   description="用例执行情况")
 runner.run(discover)