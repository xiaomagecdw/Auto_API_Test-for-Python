# -*- coding:utf-8 -*-
# @Time     :2020/6/8 16:39
# @Author   :chendaiwu_biubiubiu-----
# @FileName :httprun.py
# @Sofaware :PyCharm

from flask import request
import flask, json

'''
flask: web框架， 通过flask提供的装饰器@server.route()将普通函数转化为服务
'''

#创建一个服务，把当前的Python文件到做一个一个服务
server = flask.Flask(__name__)
#@server.route()可以将普通函数转化成服务，登录接口的路径、请求方式
@server.route('/login', methods=['get', 'post'])
def login():
    #获取通过url请求传参的数据
    username = request.values.get('name')
    #获取url请求穿的密码、明文
    pwd = request.values.get('pwd')
    #判断用户名、密码都不为空
    if username and pwd:
        if username == 'xiaomagecdw' and pwd == '123456':
            result = {'code': 200, 'message': '登录成功！'}
            return json.dumps(result, ensure_ascii=False)                           #将字典转换成字符串
        else:
            result = {'code': -1, 'message': '账号或密码错误！'}
            return  json.dumps(result, ensure_ascii=False)
    else:
        result = {'code': 100001, 'message': '账号或密码不能置空！'}
        return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    server.run(port=8888, debug=True, host='127.0.0.1')



