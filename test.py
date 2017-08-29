# encoding:utf-8
import time
from config import mysqlconnection as mc

# s = "2017-01-20T09:33:18.704450+08:00"
# ts = int(time.mktime(s))
# print s

# fields = ['start_time', 'db_user', 'app_ip', 'thread_id',
#           'exec_duration', 'rows_sent', 'rows_examined', 'slow_log']

# # print ','.join(fields)

# for col in fields:
#     print col

print mc.get('Host', None)
print mc.get('User', None)
print mc.get('Pass', None)
