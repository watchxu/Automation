#! /usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests


class WeChatPub:

   s = requests.session()
   token = None

   def __init__(self):
     self.token = self.get_token("<企业ID>", "<secret>")
     print("token is " + self.token)

   def get_token(self, corpid, secret):
     url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(corpid, secret)
     rep = self.s.get(url)
     if rep.status_code == 200:
         return json.loads(rep.content)['access_token']
     else:
         print("request failed.")
         return None

   def send_msg(self, content):
     url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=" + self.token
     header = {
         "Content-Type": "application/json"
     }
     form_data = {
         "touser": "@all",
         "toparty": " PartyID1 | PartyID2 ",
         "totag": " TagID1 | TagID2 ",
         "msgtype": "textcard",
         "agentid": 1000002,
         "textcard": {
             "title": "告警通知",
             "description": content,
             "url": "URL",
             "btntxt": "更多"
         },
         "safe": 0
     }
     rep = self.s.post(url, data=json.dumps(form_data).encode('utf-8'), headers=header)
     if rep.status_code == 200:
         return json.loads(rep.content)
     else:
         print("request failed.")
         return None


if __name__ == '__main__':
    wechat = WeChatPub()
    wechat.send_msg("<div class=\"gray\">2017年06月08号</div> <div class=\"normal\">"
                    "{报警}{warning}{bss-online.BCE.cq02:instance:链路报警}{总体异常实例比例:50%}{异常(1):cq02-bce-bss-online00.cq02}{LINK_ALARM='BGP链路BGP_M3A_移动带宽的入方向超过报...}"
                    "</div><div class=\"highlight\">请尽快处理</div>")
