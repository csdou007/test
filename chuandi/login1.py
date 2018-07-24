#coding:utf-8
import unittest,requests

class Xuelogin(unittest.TestCase):
    def setUp(self):
        """初始化"""
        pass
    def test_login_01(self):
        u'''用户名密码正确，登录测试'''
        url="http://at.ilr1000.com/api/session.json"
        params={
            "username":'6502XX00100131',
            "password":'111111',
            "clinet_type":'31',
            "client_version":'3.1',
        }
        r=requests.post(url=url,json=params)
        #通过stauts_code获取响应的状态码,code进行判断，是否为200，有则表示和服务器会话是正常的
        print(r.status_code)
        self.assertEqual(r.status_code,200)
        #通过text方法获取到响应报文的内容
        repones=r.text
        print r.text
    def test_login_02(self):
        u'''密码不正确，登录测试'''
        url="http://at.ilr1000.com/api/session.json"
        params={
            "username":'6502XX00100131',
            "password":'123456',
            "clinet_type":'31',
            "client_version":'3.1',
        }
        r=requests.post(url=url,json=params)
        #通过stauts_code获取响应的状态码,code进行判断，是否为200，有则表示和服务器会话是正常的
        print(r.status_code)
        self.assertEqual(r.status_code,200)
        #通过text方法获取到响应报文的内容
        repones=r.text
        print r.text
    def tearDown(self):
         pass