#!/usr/bin/python3
import pymysql

'''
refer to: Using UTF8 with Python MySQLdb (http://www.dasprids.de/blog/2007/12/17/python-mysqldb-and-utf-8)

"UnicodeEncodeError:'latin-1' codec can't encode character ..."

This is because MySQLdb normally tries to encode everythin to latin-1. This can be fixed by executing the following commands right after you've etablished the connection:

db.set_character_set('utf8')
dbc.execute('SET NAMES utf8;')
dbc.execute('SET CHARACTER SET utf8;')
dbc.execute('SET character_set_connection=utf8;')
"db" is the result of MySQLdb.connect(), and "dbc" is the result of  db.cursor().
'''

dbip = "172.20.1.240"
dbuser = "zhangzc"
dbpwd = "123456"
dbname = "szbpaper"

# 打开数据库连接
db = pymysql.connect(dbip,dbuser,dbpwd,dbname )
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print ("Database version : %s " % data)
# 关闭数据库连接
db.close()


'''
数据库插入操作

# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
LAST_NAME, AGE, SEX, INCOME) \
VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
('Mac', 'Mohan', 20, 'M', 2000)
try:
# 执行sql语句
cursor.execute(sql)
# 执行sql语句
db.commit()
except:
# 发生错误时回滚
db.rollback()
# 关闭数据库连接
db.close()
'''


'''
数据库查询操作
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

# 打开数据库连接
db = pymysql.connect(dbip,dbuser,dbpwd,dbname )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
db.set_charset('utf8')
cursor.execute('SET NAMES utf8;')
cursor.execute('SET CHARACTER SET utf8;')
cursor.execute('SET character_set_connection=utf8;')
# SQL 查询语句
sql = """
SELECT t.id,t.title,t.channel,t.`from`,t.company,t.stockCode,t.stockName,t.jjName,t.JJCompanyName  
FROM tp_stock t
where t.`from`='中国证券报'
"""
print(sql)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        title = row[1]
        channel = row[2]
        jjname = row[7]
        jjcompanyname = row[8]
        # 打印结果
        print ("id=%d,title=%s,channel=%s,jjname=%s,jjcompanyname=%s" % \
        (id, title, channel, jjname, jjcompanyname ))
except:
    print ("Error: unable to fetch data")
# 关闭数据库连接
db.close()


'''
数据库更新操作
更新操作用于更新数据表的的数据，以下实例将 TESTDB表中的 SEX 字段全部修改为 'M'，AGE 字段递增1：

#!/usr/bin/python3
# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()
'''


'''
删除操作
删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据：

#!/usr/bin/python3
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost","testuser","test123","TESTDB" )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭连接
db.close()
'''


'''
执行事务

# SQL删除记录语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 向数据库提交
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
'''






