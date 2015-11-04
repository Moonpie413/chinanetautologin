# -*- coding:utf8 -*-
import os

import sqlite3

# 建表语句
create_table = '''
CREATE TABLE IF NOT EXISTS log_info (
    enc TEXT
)
'''

# 插入数据语句
insert_sql = 'INSERT INTO log_info (enc) VALUES (?)'

# 查询语句
query_sql = 'SELECT enc FROM log_info'

# 删除语句
delete_sql = 'DELETE FROM log_info'

if not os.path.exists('cfgfolder'):
    os.mkdir('cfgfolder')
conn = sqlite3.connect('cfgfolder/chinanet.db')
curs = conn.cursor()


def creat():
    curs.execute(create_table)


def insert(enc):
    curs.execute(insert_sql, (enc,))
    conn.commit()


def query():
    curs.execute(query_sql)
    result = curs.fetchall()
    conn.commit()
    return result


def remove():
    curs.execute(delete_sql)
    conn.commit()


def close():
    conn.close()
