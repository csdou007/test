#coding:utf-8
import unittest,requests
from libs.LoginEntity import *
from data.shuju import login
from libs.baseTest import testApi
class Xuelogin(unittest.TestCase):
    def setUp(self):
        """初始化"""
        self.entity=LoginEntity()
    def test_login_01(self):
        u'''用户名密码正确，登录测试'''
        params=self.entity.get_login_params_01()
        api=testApi(method='post',url=login.URL+login.XUE,data=params)
        apicode=api.getCode()
        print apicode
        self.assertEqual(apicode,200)
        apijson=api.getJson()
        print apijson



        # r=requests.post(url=login.URL+login.XUE,json=params)
        # #通过stauts_code获取响应的状态码,code进行判断，是否为200，有则表示和服务器会话是正常的
        # print(r.status_code)
        # self.assertEqual(r.status_code,200)
        # #通过text方法获取到响应报文的内容
        # repones=r.text
        # print r.text
    def test_login_02(self):
        u'''密码不正确，登录测试'''
        params=self.entity.get_login_params_02()
        api=testApi(method='post',url=login.URL+login.XUE,data=params)
        apicode=api.getCode()
        print apicode
        self.assertEqual(apicode,200)
        apijson=api.getJson()
        print apijson

        # r=requests.post(url=login.URL+login.XUE,json=params)
        # #通过stauts_code获取响应的状态码,code进行判断，是否为200，有则表示和服务器会话是正常的
        # print(r.status_code)
        # self.assertEqual(r.status_code,200)
        # #通过text方法获取到响应报文的内容
        # repones=r.text
        # print r.text
    def tearDown(self):
         pass