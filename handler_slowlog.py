# encoding:utf-8
import os
import sys


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
        start_time = res[3].replace(';','').split('=')[1]
        # 慢SQL语句
        slowsql = res[4]
        print start_time, db_user, app_ip, thread_id, exec_duration, rows_sent, rows_examined, slowsql
         
        # 入库
        '''
        create table slow_log(
        id bigint(11) not null unsigned auto_increment,
        
        )

        '''

        break


if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(base_dir, 'slow.log')
    # print file_name
    handler_slowlog(file_name)
