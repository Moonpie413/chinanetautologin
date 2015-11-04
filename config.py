# -*- coding:utf8 -*-
import ConfigParser
import os

__author__ = 'maroon'

config = ConfigParser.ConfigParser()
configfile = 'cfgfolder' + os.sep + 'info.cfg'


def read_config():
    with open(configfile, 'r') as f:
        config.readfp(f)
        other_user = config.get('otherAccount', 'otherUser')
        other_user_pwd = config.get('otherAccount', 'otherUserPwd')
        reg_area = config.get('otherAccount', 'regArea')
        result = (other_user, other_user_pwd, reg_area)
    return result


def config_check():
    if not os.path.exists(configfile):
        print '配置文件不存在，正在初始化'
        with open(configfile, 'w') as f:
            init_config(f)
        print '初始化成功，请编辑cfgfolder/info.cfg填入账号信息'
        return False
    else:
        try:
            for v in read_config():
                if v == '':
                    print '请完整填写配置文件'
                    return False
        except Exception as e:
            print e
    return True


def init_config(f):
    config.add_section('otherAccount')
    config.set('otherAccount', 'otherUser', '')
    config.set('otherAccount', 'otherUserPwd', '')
    config.set('otherAccount', 'regArea', '')
    config.write(f)
