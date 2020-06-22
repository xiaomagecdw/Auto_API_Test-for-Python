# -*- coding:utf-8 -*-
# @Time     :2020/6/18 18:05
# @Author   :chendaiwu_biubiubiu-----
# @FileName :AllRun.py
# @Sofaware :PyCharm

import os
import controll.HTMLTestRunner as HTMLTestRunner
import getPathInfo
import unittest
import datetime
from config import readConfig
from Utils.send_Email import send_email
import controll.log
from apscheduler.schedulers.blocking import BlockingScheduler
import pythoncom

send_email = send_email()
path = getPathInfo.get_path()
today = datetime.datetime.now().strftime('%Y%m%d')
report_path = os.path.join(path, 'Reports', today)
on_off = readConfig.ReadConfig().get_email('on_off')
Log = controll.log.logger

class AllTest():
    def __init__(self):
        global resultPath
        resultPath = os.path.join(report_path,  'Report_'+ today + '.html')                                                           #存储报告路径
        self.caseListFile = os.path.join(path, 'Datas', 'testfile.txt')                                                 #配置执行那些测试文件的配置文件路径
        self.caseFile = os.path.join(path, 'testcases')
        self.caseList = []

        Log.info('resultPath'+resultPath)
        Log.info('caseListFile'+self.caseListFile)
        Log.info('caseLsit'+str(self.caseList))


    def set_case_list(self):
        """
        读取casefile.txt文中的用例名称，并添加到caselist元素组中
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):                                                                 #如果data非空或者不以#开头
                self.caseList.append(data.replace("\n", ""))                                                            #读取每行数据会将换行转换为\n，去掉每行数据中的\n
        fb.close()



    def set_case_suite(self):
        """

        :return:
        """
        self.set_case_list()                                                                                            #通过set_case_list()拿到caselist元素组
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case.split("/")[-1]                                     #通过split函数将aaa/bbb分割字符串，-1取后一位值
            print(case_name + '.py')                                             #打印出取出来的用例名称
            # 批量加载用例，第一个参数为用例存放路径，第一个参数为路径文件名
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)                                       #将discover存入suite_module元素组
            # print('suite_module:' + str(suite_module))
        if len(suite_module) > 0:                                               #判断suite_module元素组是否存在元素
            for suite in suite_module:                                          #如果存在，循环取出元素组内容，命名为suite
                for test_name in  suite:                                        #从discover中取出test_name，使用addTest添加到测试集
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite


    def run(self):
        """
        run test
        :return:
        """
        try:
            suite = self.set_case_suite()
            # print('try')
            # print(str(suite))
            if suite is not None:
                # print('if-suite')
                if os.path.exists(report_path)  == True:                                #判断是否有该文件，没有则创建
                    pass
                    # print("该路径已存在，继续执行！")
                else:
                    os.mkdir(report_path)
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test_Report', description='Test Description')
                runner.run(suite)
            else:
                print("Have no case to case!")
        except Exception as ex:
            print(str(ex))
            Log.info(str(ex))

        finally:
            print("**********TEST END***********")
            Log.info("**********TEST END***********")
            fp.close()

        if on_off == 'off':
            send_email.Outlook()
        else:
            print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告!")

if __name__ == '__main__':
    AllTest().run()

