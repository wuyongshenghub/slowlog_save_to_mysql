"# slowlog-into-mysql" 
'''
慢查询格式如下：
# Time: 2017-01-20T09:33:18.704450+08:00
# User@Host: test_user_db[test_user_db] @  [10.205.52.24]  Id: 137686
# Query_time: 1.782185  Lock_time: 0.000094 Rows_sent: 22459  Rows_examined: 22459
SET timestamp=1484875998;
SELECT * FROM dbname.table_name;
描述：
定义分组列表sql = []
将每个分组列表组合 sqltxt = []
sqltxt.append(sql)
分组标示isflag = 1
遍历每行，过滤SET timestamp开头内容，把开头# 至;结尾 作为一组列表

慢查询日志表结构
create table tbl_slow_log(
id bigint(11) not null auto_increment primary key,
log_time varchar(50) not null default '',
log_user varchar(50) not null default '',
query_time varchar(20) not null default '',
lock_time varchar(20) not null default '',
rows_sent varchar(20) not null default '',
row_examined varchar(20) not null default '',
log_timestamp int(11) not null default 0,
sqltxt varchar(200) not null default ''
)engine=innodb default charset=utf8;
'''
