import pymysql


# 连接 Mysql以字典形式返回数据表的字段


def mysql(host, user, password, db, tablename):
    mysql = {}
    conn = pymysql.connect(host=host,
                           user=user,
                           password=password,
                           db=db,
                           autocommit=True)
    cur = conn.cursor()
    sql = "select * from {TableName} limit 1".format(TableName=tablename)
    result = cur.execute(sql)
    desc = cur.description
    for field in desc:
        mysql[field[0]] = ""
        # print(field[0])
    cur.close()
    conn.close()
    return mysql
