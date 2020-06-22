# -*- coding:utf-8 -*-
# @Time     :2020/6/18 11:09
# @Author   :chendaiwu_biubiubiu-----
# @FileName :Http_Methods.py
# @Sofaware :PyCharm


import requests
import json

class Http_Main():

    def send_post(self, url, data):                                                 #定义psost方法，传入url地址和data值
        result = requests.post(url=url, data=data).json()                           #封装post方法，不能把参数写死
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):                                                  #定义get方法，传入URL地址和data值
        result = requests.get(url=url, data=data).json()
        res = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
        return res

    def run_main(self, method, url = None, data = None):                            #定义一个运行方法，通过method传入不同post和get方法
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url, data)
        else:
            print("method值不对，请检查！")
        return result


if __name__ == '__main__':
    result1 = Http_Main().run_main('post', 'http://127.0.0.1:8888/login', {'name':'xiaomagecdw', 'pwd':'123456'})
    result2 = Http_Main().run_main('get', 'http://127.0.0.1:8888/login', 'name=xiaomagecdw&pwd=123456')
    print(result1)
    print(result2)