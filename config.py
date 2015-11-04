# -*- coding:utf8 -*-
import ConfigParser
import os

__author__ = 'maroon'

config = ConfigParser.ConfigParser()
configfile = 'cfgfolder/info.cfg'


def read_config():
    with open('cfgfolder/info.cfg', 'r') as f:
        config.readfp(f)
        otherUser = config.get('otherAccount', 'otherUser')
        otherUserPwd = config.get('otherAccount', 'otherUserPwd')
        regArea = config.get('otherAccount', 'regArea')
        result = (otherUser,otherUserPwd,regArea)
    return result


def config_check():
    if not os.path.exists(configfile):
        print '配置文件不存在，正在初始化'
        os.mknod(configfile)
        init_config()
        print '初始化成功，请编辑cfgfolder/info.cfg填入账号信息'
        return False
    else:
        for v in read_config():
            if v == '':
                print '请完整填写配置文件'
                return False
    return True


def init_config():
    with open(configfile, 'rw+') as f:
        config.readfp(f)
        config.add_section('otherAccount')
        config.set('otherAccount', 'otherUser', '')
        config.set('otherAccount', 'otherUserPwd', '')
        config.set('otherAccount', 'regArea', '')
        config.write(f)

