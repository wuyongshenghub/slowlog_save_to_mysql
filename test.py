# encoding:utf-8
# from dateutil import tz
# from datetime import datetime

# # UTC Zone
# from_zone = tz.gettz('UTC')
# # China Zone
# to_zone = tz.gettz('CST')

# utc = datetime.utcnow()

# # Tell the datetime object that it's in UTC time zone
# utc = utc.replace(tzinfo=from_zone)

# # Convert time zone
# local = utc.astimezone(to_zone)
# print datetime.strftime(local, "%Y-%m-%d %H:%M:%S")


import time
s = "2017-01-20T09:33:18.704450+08:00"
tt = s.mktime(s)
print tt
