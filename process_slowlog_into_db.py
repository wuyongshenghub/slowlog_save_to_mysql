# encoding:utf-8

"""
python script slow.log load.sql

"""

import os
import sys
from sys import argv
# script, slowlog, sqlfile = argv

# print script, slowlog, sqlfile


line_status = 0
line_list = []


def process_timesamp(l):
    # 处理SET timestamp
    if l.startswith('SET timestamp='):
        res = l.replace(';', '').split('=')
        return [res[1]]


def process_sql_statement(l):
    # 获取SQL 语句
    return [l]


def process_time(l):
    # # Time:
    if l.startswith('# Time:'):
        res = l.replace(' ', '').strip().split('Time:')[1]
        return [res]


def process_user_host(l):
    # user@host|Id
    if l.startswith('# User@Host'):
        res = l.replace(' ', '').replace('Id', '').split(':')
        return [res[1], res[2]]


def process_querylock_time(l):
    # 处理Query_time 这一行
    if l.startswith('# Query_time:'):
        res = l.replace('# ', '').split()
        return [res[1], res[3], res[5], res[7]]


def process_row_by_row(l):
    global line_status
    # pass
    if l.find('#') >= 0 and l.find('Time:') >= 0:
        return process_time(l)
    elif l.find('#') >= 0 and l.find('User@Host:') > 0 and l.find('Id:') >= 0:
        return process_user_host(l)
    elif l.find('#') >= 0 and l.find('Query_time:') >= 0 and l.find('Lock_time:') >= 0 and l.find('Rows_sent:') >= 0 and l.find('Rows_examined:') >= 0:
        return process_querylock_time(l)
    elif l.find('SET') >= 0 and l.find('timestamp=') >= 0:
        return process_timesamp(l)
    else:
        line_status = 4
        return process_sql_statement(l)


def combine_query_statement(line_list):
    # pass
    output = ''
    for col in line_list:
        output += col + "','"
    return "('" + output.rstrip("'").rstrip(",") + ")"

slowlog = 'slow.log'
f = open(str(slowlog), 'r')
while True:
    # pass
    line = f.readline()
    if not line:
        break
    l = line.strip()
    tmp_list = process_row_by_row(l)
    line_list.append(tmp_list)

arr = line_list

# 将line_list 转换成SQL 格式
