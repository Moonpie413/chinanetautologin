# -*- coding:utf8 -*-
# userName=hswl00002832&password=677454&regArea=ah&userIp=&basIp=&acName=&oraUrl=&loginMode=2

import socket
import os
import urllib
import urllib2
import cookielib

if os.name != "nt":
    import fcntl
    import struct

class connect(object):
    def __init__(self):
        self.request_url = 'https://wlan.ct10000.com/login.wlan'
        self.otherUser = 'hswl00002832'
        self.otherUserPwd = '677454'
        self.regArea = 'ah';

    def login(self):
        cookie = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookie)
        opener = urllib2.build_opener(handler)
        opener.addheaders

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0',
            'Host' : 'wlan.ct10000.com',
            'Connection' : 'keep-alive',
            'Referer' : 'https://wlan.ct10000.com/index.wlan'
        }

        data = {
            'userName' : self.otherUser ,
            'password' : self.otherUserPwd ,
            'regArea' : self.regArea ,
            'userIp' : '' ,
            'basIp' : '' ,
            'acName' : '' ,
            'oraUrl' : '' ,
            'loginMode' : '2'
        }

        for key,value in headers.iteritems():
            temp = (key,value)
            opener.addheaders.append(temp)

        post_data = urllib.urlencode(data)
        response = opener.open(self.request_url,post_data)
        return response

login = connect()
f = login.login()
print f.read()
