# encoding:utf-8
import os
import sys
import MySQLdb
from config import mysqlconnection as mc

reload(sys)
sys.setdefaultencoding('utf8')

# 连接数据库
try:
    conn = MySQLdb.connect(host=mc.get('Host', None), port=mc.get('Port', None),
                           user=mc.get('User', None), passwd=mc.get('Pass', None), db=mc.get('db', None), charset='utf8')
    conn.autocommit(True)
except Exception as e:
    print e


def read_slow_log_to_list(file_name):
    # 组合每一分列表[],[]...
    sqltxt = []
    # 每组分列表
    sql = []
    # 拼接多个SQL语句
    output = ''
    # 设置分组列表标识
    isflag = 1
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                sql.append(line)
            elif line.startswith('SET'):
                sql.append(line)
            elif line.startswith('USE'):
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

    return sqltxt


def handler_slowlog(file_name):
    slow_info = []
    res = read_slow_log_to_list(file_name)
    for res in res:
        # print res
        # time = res[0]
        # User@Host 信息
        userhost = res[1]
        # 连接数据库用户
        db_user = userhost.replace('# User@Host:', '').split('[')[0]
        # 应用程序连接DB所在的ip
        app_ip = userhost.replace('# User@Host:', '').split()[
            2].replace('[', '').replace(']', '')
        # 开启线程id
        thread_id = userhost.replace('# User@Host:', '').split(':')[1]
        # print db_user, app_ip, thread_id
        querytime = res[2]
        # 执行持续时长
        exec_duration = querytime.replace('# ', '').split()[1]
        # 执行结果集返回行数
        rows_sent = querytime.replace('# ', '').split()[5]
        # 完成查询需要评估行数量
        rows_examined = querytime.replace('# ', '').split()[7]
        # print exec_duration, rows_sent, rows_examined
        # 开始时间
        start_time = res[3].replace(';', '').split('=')[1]
        # 慢SQL语句
        slowsql = res[4]
        # print start_time, db_user, app_ip, thread_id, exec_duration, rows_sent, rows_examined, slowsql
        tmp = (start_time, db_user, app_ip, thread_id,
               exec_duration, rows_sent, rows_examined, slowsql)
        slow_info.append(tmp)
        # break
    return slow_info


def do_save_to_mysql(table, fields, param):
    sql = "insert into %s(%s) values %s" % (table, fields, param)
    # print sql
    cur = conn.cursor()
    try:
        cur.execute(sql)
    except Exception as e:
        print "入库错误:%s" % (e)


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(base_dir, 'slow.log')
    # 返回慢查询日志文件中处理后的各列数据
    res = handler_slowlog(file_name)
    # 表中需要插入数据的列名
    fields = ['start_time', 'db_user', 'app_ip', 'thread_id',
              'exec_duration', 'rows_sent', 'rows_examined', 'slowsql']

    数据入库
    for val in res:
        do_save_to_mysql('slow_log', ','.join(fields), val)
