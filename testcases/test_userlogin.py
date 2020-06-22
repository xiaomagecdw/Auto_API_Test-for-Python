# -*- coding:utf-8 -*-
# @Time     :2020/6/18 11:54
# @Author   :chendaiwu_biubiubiu-----
# @FileName :test_userlogin.py
# @Sofaware :PyCharm





import json
import unittest
import urllib.parse
import paramunittest as paramunittest
from Utils import GetURLGarams,ReadExcel
from controll.Http_Methods import Http_Main


url = GetURLGarams.geturlgarams().get_url()
excel = ReadExcel.ReadExcel().read_excel('case.xlsx', 'case')

@paramunittest.parametrized(*excel)
class test_userlogin(unittest.TestCase):

    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path:
        :param query:
        :param method:
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """

        :return:
        """
        print(self.case_name + '测试开始前的准备。')

    def test_userlogin(self):
        self.checkResult()

    def tearDown(self):
        print('测试结束，输出log完结！\n\n')

    def checkResult(self):
        """
        check test result
        :return:
        """
        url1 = "http://www.xxx.com/login?"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))                                      #将一个完整的url中的name和pwd转换为{'name':'xxx','pwd:'xxx'}
        info = Http_Main().run_main(self.method, url, data1)                                                            #根据excel中的method调用run_main进行request请求，并拿到响应
        ss = json.loads(info)                                                                                           #将响应转换为字典格式
        if self.case_name == 'login_successfull':                                                                                #如果case_name是login，说明合法，返回code应该为200
            self.assertEqual(ss['code'], 200)
        if self.case_name == 'username_error' or self.case_name == 'password_error':
            self.assertEqual(ss['code'], -1)
        if self.case_name == 'username_noll' or self.case_name == 'password_noll':
            self.assertEqual(ss['code'], 100001)


if __name__ == '__main__':
    test_userlogin().run()