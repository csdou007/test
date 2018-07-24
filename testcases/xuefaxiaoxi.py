#coding:utf-8
import unittest,requests
from libs.XiaoxiEntity import *
from data.shuju import *
from chuandi.studenttoken import token
from libs.baseTest import testApi
class Xuelogin(unittest.TestCase):
    def setUp(self):
        """初始化"""
        self.xentity=XiaoxiEntity()
    def test_xiaoxi_01(self):
        u'''学生给家长发消息,标题、接收者、发送内容格式正确测试'''
        params=self.xentity.get_Xiaoxi_params_01()
        n=token().testLoginApi()
        api=testApi(method='post',url=(xiaoxi.URL+xiaoxi.Xi+n),data=params)
        apicode=api.getCode()
        print apicode
        self.assertEqual(apicode,200)
        apijson=api.getJson()
        print apijson


        # r=requests.post(url=xiaoxi.URL+xiaoxi.Xi+n,json=params)
        # #通过stauts_code获取响应的状态码,code进行判断，是否为200，有则表示和服务器会话是正常的
        # print(r.status_code)
        # self.assertEqual(r.status_code,200)
        # #通过text方法获取到响应报文的内容
        # repones=r.text
        # print r.text
    def test_xiaoxi_02(self):
        u'''学生给家长发消息,接收者id不正确测试'''
        params=self.xentity.get_Xiaoxi_params_02()
        n=token().testLoginApi()
        api=testApi(method='post',url=xiaoxi.URL+xiaoxi.Xi+n,data=params)
        apicode=api.getCode()
        print apicode
        self.assertEqual(apicode,200)
        apijson=api.getJson()
        print apijson


        # n=token().testLoginApi()
        # r=requests.post(url=xiaoxi.URL+xiaoxi.Xi+n,json=params)
        # #通过stauts_code获取响应的状态码,code进行判断，是否为200，有则表示和服务器会话是正常的
        # print(r.status_code)
        # self.assertEqual(r.status_code,200)
        # #通过text方法获取到响应报文的内容
        # repones=r.text
        # print r.text
    def tearDown(self):
         pass