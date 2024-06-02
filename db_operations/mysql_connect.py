import pymysql

connect = pymysql.connect(host='123.57.135.65', port=3306, db='test',
                          user='root', passwd='songj1', charset='utf8')
cursor = connect.cursor()
cursor.execute('select * from student')
fetchone = cursor.fetchone()
# cursor.execute("DROP TABLE IF EXISTS config_info")
# create_config_info = '''/******************************************/
# /*   表名称 = config_info                  */
# /******************************************/
# CREATE TABLE `config_info` (
#   `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
#   `data_id` varchar(255) NOT NULL COMMENT 'data_id',
#   `group_id` varchar(128) DEFAULT NULL COMMENT 'group_id',
#   `content` longtext NOT NULL COMMENT 'content',
#   `md5` varchar(32) DEFAULT NULL COMMENT 'md5',
#   `gmt_create` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
#   `gmt_modified` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
#   `src_user` text COMMENT 'source user',
#   `src_ip` varchar(50) DEFAULT NULL COMMENT 'source ip',
#   `app_name` varchar(128) DEFAULT NULL COMMENT 'app_name',
#   `tenant_id` varchar(128) DEFAULT '' COMMENT '租户字段',
#   `c_desc` varchar(256) DEFAULT NULL COMMENT 'configuration description',
#   `c_use` varchar(64) DEFAULT NULL COMMENT 'configuration usage',
#   `effect` varchar(64) DEFAULT NULL COMMENT '配置生效的描述',
#   `type` varchar(64) DEFAULT NULL COMMENT '配置的类型',
#   `c_schema` text COMMENT '配置的模式',
#   `encrypted_data_key` varchar(1024) NOT NULL DEFAULT '' COMMENT '密钥',
#   PRIMARY KEY (`id`),
#   UNIQUE KEY `uk_configinfo_datagrouptenant` (`data_id`,`group_id`,`tenant_id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='config_info';'''
# cursor.execute(create_config_info)
data = [('a', 10, 20, 30),
        ('b', 10, 20, 30)]
sql = "INSERT INTO student (name,chinese,english,math) VALUES (%s, %s, %s, %s)"
try:
    cursor.executemany(sql, data)
    connect.commit()
except:
    connect.rollback()
    raise
print(fetchone)
# mysql like查询2种方式
sel = "风"
sql_like1 = "SELECT * FROM student WHERE name LIKE '%s'" % ('%%%s%%' % sel)
# sql_like2 = "SELECT * FROM student WHERE name LIKE '%%%%%s%%%%'" % sel
cursor.execute(sql_like1)
# cursor.execute(sql_like2)
data = cursor.fetchall()
print(data)
