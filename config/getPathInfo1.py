# -*- coding:utf-8 -*-
# @Time     :2020/6/17 17:26
# @Author   :chendaiwu_biubiubiu-----
# @FileName :getPathInfo1.py
# @Sofaware :PyCharm

import os

'''
获取配置文件路径
'''
def get_path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path

if __name__ == '__main__':
    print('测试文件路径是否ok！，路径为：', get_path())