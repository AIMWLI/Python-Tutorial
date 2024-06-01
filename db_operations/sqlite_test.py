import sqlite3

# 连接到sqlite数据库, 数据库文件是test.db, 如果文件不存在则创建
connect = sqlite3.connect('test')
# 创建一个cursor游标对象
cursor = connect.cursor()
# cursor.execute('create table user(id int (10) primary key, name varchar(20) not null)')
cursor.execute('insert into user (id,name) values (1,"taylor")')
cursor.execute('insert into user (id,name) values (2,"tony")')
cursor.execute('insert into user (id,name) values (3,"bob")')
# cursor.execute("select * from user where id > ?", (1,))  # 问号作为占位符避免sql注入, 元组替换问号(不要忽略元组中最后的逗号)
# cursor.execute('update user set name = ? where id = ?',('swift',1))
execute = cursor.execute("select * from user")
fetchall = cursor.fetchall()
print(fetchall)
cursor.close()
connect.close()
