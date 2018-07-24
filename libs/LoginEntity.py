#coding:utf-8
import json
from data import shuju

class LoginEntity(object):
    def get_login_params_01(self):
        """登录接口，用户名和密码正确"""
        # 1.post的body是json类型，也可以用json参数传入。
        # 2.先导入json模块，用dumps方法转化成json格式。
        # 3.返回结果，传到data里。
        # 字典和json数据格式都是key:value的形式，而json是数据打包的一种格式，并不像字典具备操作性
        #Python中提供了json.load()转换函数，方便json数据的调用
        #json的格式要求必须且只能使用双引号作为key或者值的边界符号，不能使用单引号，而且“key”必须使用边界符（双引号），但字典就无所谓了。
        headers={"Content-Type": "application/json;charset=utf-8"
               }
        params={
            "username":'6502XX00100131',
            "password":'111111',
            "clinet_type":'31',
            "client_version":'3.1',
        }
        print type(params)
        print params
        data=json.dumps(params)
        data=json.loads(data)
        # data["username"]='6502XX00100131'
        # data["password"]='111111'
        # data["clinet_type"]='31'
        # data["client_version"]='3.1'
        print type(data)
        print data
        return data
    def get_login_params_02(self):
        '''登录接口，密码不正确'''

        headers={"Content-Type": "application/json;charset=utf-8"
               }
        params={
            "username":'6502XX00100131',
            "password":'123456',
            "clinet_type":'31',
            "client_version":'3.1',
        }
        data=json.dumps(params)
        data=json.loads(data)
        # data["username"]='6502XX00100131'
        # data["password"]='123456'
        # data["clinet_type"]='31'
        # data["client_version"]='3.1'
        print type(data)
        print data
        return data
if __name__ =="__main__":
    t = LoginEntity()
    t.get_login_params_01()
    t.get_login_params_02()