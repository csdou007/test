#coding:utf-8
import json
from data import shuju
from chuandi.jiazhangid import jiazhang

class XiaoxiEntity(object):
    def get_Xiaoxi_params_01(self):
        """学生给家长发消息,标题、接收者、发送内容格式正确"""

        headers={"Content-Type": "application/json;charset=utf-8"
               }
        m=jiazhang().jia()
        params={
             "title":"",
             "receivers":"",
             "content":""
                }
        data=json.dumps(params)
        data=json.loads(data)
        data["title"]='autotest'
        data["receivers"]=[m]
        data["content"]='test content'
        print type(data)
        print data
        return data
    def get_Xiaoxi_params_02(self):
        '''学生给家长发消息,接收者id不正确'''

        headers={"Content-Type": "application/json;charset=utf-8"
               }
        params={
             "title":"",
             "receivers":"",
             "content":""
                }
        data=json.dumps(params)
        data=json.loads(data)
        data["title"]='autotest'
        data["receivers"]='ddddd'
        data["content"]='test content'
        print type(data)
        print data
        return data
if __name__ =="__main__":
    t = XiaoxiEntity()
    t.get_Xiaoxi_params_01()
    t.get_Xiaoxi_params_02()