# encoding:utf-8
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(base_dir, 'slow.log')

sqltxt = []
sql = []
output = ''
isflag = 1
with open(file_name) as f:
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            sql.append(line)
        elif line.startswith('SET') or line.startswith('USE'):
            continue
        else:
            if line.endswith(';'):
                if len(output) == 0:
                    sql.append(line)
                    isflag = 0
                else:
                    line = output + ' ' + line
                    sql.append(line)
                    output = ''
                    isflag = 0
            else:
                output += str(' ') + line
        if isflag == 0:
            sqltxt.append(sql)
            isflag = 1
            sql = []

print sqltxt

# def read_slowlog(file_name):
#         # isflag = 0
#     res = []
#     with open(file_name) as f:
#         for lines in f:
#             res.append(lines)
#     return res


# def handler_slow_log(file_name):
# 	isflag = 0
# 	sqltxt = ''
#     lines = read_slowlog(file_name)
#     for l in lines:


# if __name__ == '__main__':
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     file_name = os.path.join(base_dir, 'slow.log')
#     # print file_name
#     handler_slow_log(file_name)
