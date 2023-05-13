import pymysql
"""连接一个数据库，并创建表"""
mysql_connection = pymysql.connect(host= '127.0.0.1', port= 3306, user= 'root', password= '183655', db= 'virus_db')# 连接数据库
cur = mysql_connection.cursor() #创建游标
sql = """
    create table test(
    region varchar(20) NOT NULL COMMENT '地区',
    num int NOT NULL COMMENT '患病人数'
    )
""" # 要执行的sql语句
# 异常捕获处理
try:
    cur.execute(sql) # 通过游标执行语句
    print("创建表成功")
except Exception as e: # 若try中语句发生异常的异常处理
    print(e)
    print("创建表失败")
finally: # 无论是否异常都执行的语句
    cur.close() # 关闭游标
    mysql_connection.close() # 关闭数据库连接
