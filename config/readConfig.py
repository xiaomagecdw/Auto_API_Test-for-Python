# -*- coding:utf-8 -*-
# @Time     :2020/6/17 17:15
# @Author   :chendaiwu_biubiubiu-----
# @FileName :readConfig.py
# @Sofaware :PyCharm

import os
# from config import getPathInfo1
import getPathInfo
import configparser

path = getPathInfo.get_path()                                     #调用实例恶化，该类返回的路径是：H:\Auto_API_test\config
config_path = os.path.join(path, 'config', 'config.ini')                     #在返回该路径下增加一级，路径为：H:\Auto_API_test\config\config.ini
config = configparser.ConfigParser()                              #调用外部配置文件的方法
config.read(config_path, encoding = 'utf-8')

class ReadConfig():

    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':
    print('HTTP中的baseurl地址是：', ReadConfig().get_http('baseurl'))





