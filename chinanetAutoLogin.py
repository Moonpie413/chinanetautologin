# -*- coding:utf8 -*-

import urllib
import urllib2
import cookielib
import json
import ssl
import sqlunit


class Connect(object):
    def __init__(self):
        # 关闭证书验证
        ssl._create_default_https_context = ssl._create_unverified_context
        # 如果表不存在则建表
        sqlunit.creat()

        self.request_url = 'https://wlan.ct10000.com/login.wlan'
        self.logout_url = 'https://wlan.ct10000.com/logout.wlan'
        self.otherUser = 'hswl00002402'
        self.otherUserPwd = '253540'
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
        try:
            response = self.opener.open(self.request_url, post_data)
            return response.read()
        except urllib2.HTTPError as e:
            if e.code == 500:
                print '服务器无响应，请稍后再试'
                exit()
            else:
                print '服务器错误，状态码: ' + e.code
                exit()
        except urllib2.URLError as e:
            print '服务器错误,错误原因: ' + e.reason
            exit()

    def logout(self, enc_str):

        data = {
            'Enc': enc_str
        }

        post_data = urllib.urlencode(data)

        # 建立连接，返回response
        try:
            response = self.opener.open(self.logout_url, post_data)
            return response.read()
        except urllib2.HTTPError as e:
            if e.code == 500:
                print '服务器无响应，请稍后再试'
                exit()
            else:
                print '服务器错误，状态码: ' + e.code
                exit()
        except urllib2.URLError as e:
            print '服务器错误,错误原因: ' + e.reason
            exit()

    # 处理response
    def response_handle(self, response):
        # 将response字符串转为字典
        response_dict = json.loads(response)
        suc_state = response_dict['sucState']
        resp_code = response_dict['respCode']
        enc_str = response_dict['encStr']
        if suc_state == 'SUCCESS' and resp_code == '0':
            if enc_str:
                print '连接成功'
                return enc_str
            else:
                print '断开成功'
                self.cookie.clear()
        if suc_state == 'FAIL':
            print '请求失败，错误代码为: ' + str(resp_code)


def main():
    connect = Connect()
    result = sqlunit.query()
    if result:
        print '正在断开...'
        enc_str = ''.join(result.pop())
        response = connect.logout(enc_str)

    else:
        print '正在连接...'
        response = connect.login()

    handle_result = connect.response_handle(response)
    if handle_result:
        sqlunit.insert(handle_result)
    else:
        sqlunit.remove()
    sqlunit.close()

if __name__ == '__main__':
    main()


