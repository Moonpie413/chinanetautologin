# -*- coding:utf8 -*-

import urllib
import urllib2
import cookielib
import json
import ssl


class Connect(object):
    def __init__(self):
        # 关闭证书验证
        ssl._create_default_https_context = ssl._create_unverified_context

        self.request_url = 'https://wlan.ct10000.com/login.wlan'
        self.logout_url = 'https://wlan.ct10000.com/logout.wlan'
        self.otherUser = 'hswl00002832'
        self.otherUserPwd = '677454'
        self.regArea = 'ah'

        # 初始化cookie
        self.cookie = cookielib.CookieJar()
        # 初始化cookiehandler
        self.handler = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.handler)

    def login(self):

        # 头信息
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Host': 'wlan.ct10000.com',
            'Connection': 'keep-alive',
            'Referer': 'https://wlan.ct10000.com/index.wlan'
        }

        # 数据
        data = {
            'userName': self.otherUser,
            'password': self.otherUserPwd,
            'regArea': self.regArea,
            'userIp': '',
            'basIp': '',
            'acName': '',
            'oraUrl': '',
            'loginMode': '2'
        }

        # 迭代添加头信息
        for key, value in headers.iteritems():
            # 用元组的形式添加headers
            temp = (key, value)
            self.opener.addheaders.append(temp)

        post_data = urllib.urlencode(data)

        # 建立连接，返回response
        response = self.opener.open(self.request_url, post_data)
        return response.read()

    def logout(self):
        with open('./Enc.txt') as f:
            enc_str = f.readline()
        data = {
            'Enc': enc_str
        }

        post_data = urllib.urlencode(data)

        # 建立连接，返回response
        response = self.opener.open(self.logout_url, post_data)
        return response.read()


# 处理response
def response_handle(response):
    # 将response字符串转为字典
    response_dict = json.loads(response)
    susstate = response_dict['sucState']
    respcode = response_dict['respcode']
    encstr = response_dict['encstr']
    if susstate == 'SUCCESS' and respcode == '0':
        if encstr:
            print '连接成功'
            with open('./Enc.txt', 'w') as f:
                f.write(encstr)
        else:
            print '断开成功'
    if susstate == 'FAIL' and respcode == '202':
        print '连接失败'

# 简单测试
connect = Connect()
f = connect.login()
response_handle(f)
