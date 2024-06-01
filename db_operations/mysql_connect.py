import pymysql

connect = pymysql.connect(host='123.57.135.64', port=3306, db='test', user='root', passwd='songjin1', charset='utf8',
                          cursorclass=pymysql.cursors.DictCursor)
