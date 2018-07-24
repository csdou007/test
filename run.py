#-*- coding:utf-8 -*-
import unittest
import HTMLTestRunner
import os,time
list="F:\\jkceshi\\testcases"
REPORT_PATH = "F:\\jkceshi\\report\\testreport"
def createsuit():
    testunit=unittest.TestSuite()#初始化一个测试套件

    discover=unittest.defaultTestLoader.discover(list,pattern='*.py',top_level_dir=None)
    #diascover加载测试用例,discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里，这样就可以用unittest里面的TextTestRunner这里类的run方法去执行
    # 构建suite suite = unittest.TestLoader().discover("testsuites")
    #将discover()筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:

            testunit.addTest(test_case)
            print(testunit)
    return testunit
alltestnames=createsuit()

#创建测试报告文件
now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))# 获取系统当前时间
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
result_dir = REPORT_PATH + day
# 设置报告名称格式
if os.path.exists(result_dir):

    filename=result_dir+"\\"+now+'report.html'
    fp=file(filename,'wb')
    #打开文件open()是file()的别名,以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件
                                                         #如果文件已存在，先清空，再打开文件
     #定义测试报告,初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                       title=u'接口测试',
                                                       description=u'用例执行情况:')
    runner.run(alltestnames)
    fp.close()
else:
    os.mkdir(result_dir)
    filename=result_dir+"\\"+now+'report.html'
    fp=file(filename,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                       title=u'接口测试',
                                                       description=u'用例执行情况:')

    runner.run(alltestnames)
    fp.close()