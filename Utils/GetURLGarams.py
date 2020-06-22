# -*- coding:utf-8 -*-
# @Time     :2020/6/18 11:41
# @Author   :chendaiwu_biubiubiu-----
# @FileName :GetURLGarams.py
# @Sofaware :PyCharm

from config import readConfig
# from logging import logger

readconfig = readConfig.ReadConfig()

class geturlgarams():

    def get_url(self):
        new_url = readconfig.get_http('scheme') + '://' + readconfig.get_http('baseurl') + ':8888' + '/login' + '?'
        # logger.info('new_url':new_url)
        return new_url


if __name__ == '__main__':
    print(geturlgarams().get_url())