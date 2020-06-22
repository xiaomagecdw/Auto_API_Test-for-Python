# -*- coding:utf-8 -*-
# @Time     :2020/6/18 14:53
# @Author   :chendaiwu_biubiubiu-----
# @FileName :send_Email.py
# @Sofaware :PyCharm


import os
import datetime
import win32com.client as win32
from config import readConfig
import getPathInfo


read_conf = readConfig.ReadConfig()
subject = read_conf.get_email('subject')                                            #从配置文件中读取邮件主题
app = read_conf.get_email('app')                                                    #从配置文件中获取邮件类型
addresses = read_conf.get_email('addresses')
copy = read_conf.get_email('copy')
today = datetime.datetime.now().strftime('%Y%m%d')
mail_path = os.path.join(getPathInfo.get_path(), 'Reports', today, 'Report_'+ today + '.html')

class send_email():
    def Outlook(self):
        outlook = win32.Dispatch("%s.Application" % app)
        # outlook = win32.Dispatch("Foxmail.Application")
        mail = outlook.CreateItem(0)
        # mail = outlook.CreateItem(win32.constants.olMailItem)
        mail.To = addresses
        mail.CC = copy
        mail.subject = str(datetime.datetime.now())[0:19] + '_'+'%s' % subject
        mail.Attachments.Add(mail_path, 1, 1, "Myfile")
        content = """
XXXX,您好：
    自动化接口测试已完成，请查收测试结果，详情请查看附件！
    报告已邮件发送！！
                    """
        mail.Body = content
        mail.Send()


if __name__ == '__main__':
    print(subject)
    send_email().Outlook()
    print("send email ok ......")