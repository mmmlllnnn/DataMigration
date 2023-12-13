import mongo as mongo
import mysql as mysql
import judesimilar as judesimilar
import pymongo
from configparser import ConfigParser
#读取数据库配置区
conf=ConfigParser()
conf.read("C:/Users/flash\Desktop/Flash项目汇集处/Migration 1.2.2/conf.ini",encoding='utf-8')
result1={'$project':''}#第一层语句==从 Mongodb中拿数
result2={'$project':''}#第二层语句==从 Mysql中取字段,智能对应上一层的字段
mongoUrl = conf['mongo']['mongoUrl']
mongoDbName = conf['mongo']['mongoDbName']
# mongoTableName = 'test'
mysqlHost = conf['mysql']['mysqlHost']
mysqlUser = conf['mysql']['mysqlUser']
mysqlPassword = conf['mysql']['mysqlPassword']
mysqlDb = conf['mysql']['mysqlDb']
# mysqlTableName='last'



def getResult(mongoTableName=None,mysqlTableName=None,confidence=None):
    # 获得 MongoDB结果字典
    Mongo={}
    Mysql={}
    m = []
    similar_result = {}
    client = pymongo.MongoClient(mongoUrl)
    db = client.get_database(mongoDbName)
    if mongoTableName!='':
        collection = db.get_collection(mongoTableName)
        resp = collection.find_one()  # 得到了一个全体结构的字典====解析它
        client.close()
        dt = mongo.Dict(resp)
        dt.cle()
        Mongo = dt.main()
        b = Mongo.keys()
        for i in b:
            m.append(i)
    # 获得 Mysql结果字典
    if mysqlTableName!='':
        Mysql = mysql.mysql(mysqlHost,mysqlUser,mysqlPassword,mysqlDb,mysqlTableName)
        a = Mysql.keys()
        # 获得二者中相似度最高的字段对应
        for i in a:
            temPor = judesimilar.similar(i, m,confidence)
            similar_result[i] = "${temPor}".format(temPor=temPor)
            if temPor == '':
                similar_result[i] = ''
            else:#Mongo[temPor]
                # similar_result[i] = "${temPor}".format(temPor=temPor)
                similar_result[i] = "{temPor}".format(temPor=Mongo[temPor])
    
    #结果语句输出区
    # print("db.{db}.aggregate(".format(db=mongoTableName))
    result1['$project']=Mongo
    result2['$project']=similar_result
    # print(result1,",",'\n')
    # print(result2)
    # print(")"){} {}
    if (len(Mongo)!=0)&(not similar_result):
        return result1
    else:
        return result2


# getResult('rent_collection','rent_collection_cashflows',70)