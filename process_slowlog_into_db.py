# encoding:utf-8

"""
python script slow.log load.sql

"""

import os
import sys
from sys import argv
# script, slowlog, sqlfile = argv

# print script, slowlog, sqlfile


def process_timesamp(l):
    pass


def process_sql_statement(l):
    pass


def process_time(l):
    # pass
    if l.startswith('# Time:'):
        res = l.replace(' ', '').strip().split('Time:')[1]
        return [res]


def process_user_host(l):
    # pass
    if l.startswith('# User@Host'):
        res = l.replace(' ', '').replace('Id', '').split(':')
        return [res[1], res[2]]


def process_querylock_time(l):
    pass


def process_row_by_row(l):
    # pass
    if l.find('#') >= 0 and l.find('Time:') >= 0:
        return process_time(l)
    elif l.find('#') >= 0 and l.find('User@Host:') > 0 and l.find('Id:') >= 0:
        print process_user_host(l)


def combine_query_statement(l):
    pass

slowlog = 'slow.log'
f = open(str(slowlog), 'r')
while True:
    # pass
    line = f.readline()
    if not line:
        break
    l = line.strip()
    tmp_list = process_row_by_row(l)
    # print tmp_list
