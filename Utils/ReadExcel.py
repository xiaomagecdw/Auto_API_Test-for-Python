# -*- coding:utf-8 -*-
# @Time     :2020/6/18 10:24
# @Author   :chendaiwu_biubiubiu-----
# @FileName :ReadExcel.py
# @Sofaware :PyCharm


import os
import xlrd
# from config import getPathInfo1
import getPathInfo

path = getPathInfo.get_path()                   #获取文件当前路径

class ReadExcel():

    def read_excel(self, excel_name, sheet_name):                                           #excel_name是用例的excel名称，sheet_name是sheet页名称
        dataset = []
        excel_path = os.path.join(path, 'Datas', excel_name)                               #获取excel文件路径
        workbook = xlrd.open_workbook(excel_path)                                           #打开excel
        sheet = workbook.sheet_by_name(sheet_name)                                          #获取sheet名称
        for n in range(sheet.nrows):                                                        #根据总行数进行循环
            if sheet.row_values(n)[0] != u'case_name':                                      #如果sheet的第一个值不等于case_name，就把盖子添加到dataset[]中
                dataset.append(sheet.row_values(n))
        return dataset


if __name__ == '__main__':
    print(ReadExcel().read_excel('case.xlsx', 'case'))
    print(ReadExcel().read_excel('case.xlsx', 'case')[0][1])
    print(ReadExcel().read_excel('case.xlsx', 'case')[1][2])

