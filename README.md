功能描述：
---
1.慢查询日志转储后记录到数据库中 <br>
2.后期分析，每天，每分钟，慢日志量绘图 <br>

主要流程：
---
1.遍历慢查询日志，将其格式一条慢查询划分为一个列表 <br>
2.格式化慢日志中每条数据，入库前准备<br>
3.入库 <br>

		慢查询格式如下：
		# Time: 2017-01-20T09:33:18.704450+08:00
		# User@Host: test_user_db[test_user_db] @  [10.205.52.24]  Id: 137686
		# Query_time: 1.782185  Lock_time: 0.000094 Rows_sent: 22459  Rows_examined: 22459
		SET timestamp=1484875998;
		SELECT * FROM dbname.table_name;

		慢查询日志表结构
		create table slow_log(
		id bigint(11) unsigned not null auto_increment,
		start_time int(11) unsigned not null default 0 comment '开始时间',
		db_user varchar(20) not null default '' comment '程序连接数据库用户名',
		app_ip varchar(15) not null default '' comment '应用服务器IP',
		thread_id int(11) unsigned not null default 0 comment '线程id',
		exec_duration decimal(8,6) not null default 0 comment 'SQL执行时长单位秒',
		rows_sent int(11) unsigned not null default 0 comment '结果集返回记录数量',
		rows_examined int(11) unsigned not null default 0 comment '评估记录数量',
		slowsql varchar(100) not null default '' comment '慢SQL语句',
		primary key(id),
		key idx_start_time(start_time)
		)engine = innodb default charset=utf8;

		实现结果：
		

