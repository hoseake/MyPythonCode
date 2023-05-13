import pymysql

"""连接一个数据库，并创建表"""
mysql_connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='183655', db='virus_db')  # 连接数据库
cur = mysql_connection.cursor()  # 创建游标
sql = """
    INSERT INTO test (region,num) value (%s,%s)
"""  # 要执行的sql语句
# 异常捕获处理
try:
    # cur.execute(sql, ('中国', 100))  # 插入一条语句
    cur.executemany(sql, [('美国', 5000000), ('中国', 100), ('日本', 5000000)])
    mysql_connection.commit()# 提交操作事务，必须语句，否则数据库实际操作不执行
    print("插入成功")
except Exception as e:  # 若try中语句发生异常的异常处理
    print(e)
    mysql_connection.rollback() # 发生错误，操作不成功时回滚，取消操作
    print("插入失败")
finally:  # 无论是否异常都执行的语句
    cur.close()  # 关闭游标
    mysql_connection.close()  # 关闭数据库连接
