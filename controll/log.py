# -*- coding:utf-8 -*-
# @Time     :2020/6/8 13:46
# @Author   :chendaiwu_biubiubiu-----
# @FileName :log.py
# @Sofaware :PyCharm


import os
import logging
import datetime
from logging.handlers import TimedRotatingFileHandler
import getPathInfo
from pathlib import Path
import sys


path = getPathInfo.get_path()
Log_path = os.path.join(path, 'log')                                    #日志存储路径


class Logger(object):
    def __init__(self, logger_name = 'logs...'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'logs'+ self.today()
        self.backup_count = 20
        self.console_output_level = 'WARNING' #DEBUG, INFO, WARNING, ERROR, CAITICAL
        self.file_output_level = 'DEBUG'
        self.formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s line:%(lineno)d: %(message)s')

    def get_logger(self):
        """
        在logger中添加日志句柄并返回，如果logger已有句柄，直接返回
        :return:
        """
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            file_handler = TimedRotatingFileHandler(filename=os.path.join(Log_path, self.log_file_name), when='D',
                                                    interval=1, backupCount=self.backup_count, delay=True,
                                                    encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

    # 获取本地时间
    def today(self):
        now = datetime.datetime.now()
        return now.strftime('%Y%m%d')

logger = Logger().get_logger()



