# -*- coding: utf-8 -*-
import os, sys
# 导入pymysql模块
import pymysql
import datetime

def getDatabases():
    # 连接database
    db = pymysql.connect('localhost', 'root', 'root')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("show databases")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    deful = ['information_schema','mysql','performance_schema','sys']
    userData = []
    for i in data:
        if i[0] not in deful:
            userData.append(i[0])
    # 关闭数据库连接
    db.close()
    return userData

def getAssetInfo(database):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from asset")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    db.close()
    jsonData = []
    for i in data:
        result = {}
        result['id'] = i[0]
        result['name'] = i[1]
        result['type'] = i[2]
        result['project'] = i[3]
        result['createtime'] = i[4].strftime('%Y/%m/%d %I:%M:%S %p')
        result['auther'] = i[5]
        jsonData.append(result)
    return jsonData
def getEpsInfo(database):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from eps")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    db.close()
    jsonData = []
    for i in data:
        result = {}
        result['id'] = i[0]
        result['number'] = i[1]
        result['createtime'] = i[2].strftime('%Y/%m/%d %I:%M:%S %p')
        # result['createtime'] = i[2]
        result['creator'] = i[3]
        result['project'] = i[4]
        jsonData.append(result)
    return jsonData
def getAssetTaskInfo(database):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from assettask")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    db.close()
    jsonData = []
    for i in data:
        result = {}
        result['id'] = i[0]
        result['chinesename'] = i[1]
        result['type'] = i[2]
        result['pipeline'] = i[3]
        result['producer'] = i[4]
        result['status'] = i[5]
        jsonData.append(result)
    return jsonData
def getShotInfo(database):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from shot")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    db.close()
    jsonData = []
    for i in data:
        result = {}
        result['id'] = i[0]
        result['shot_name'] = i[1]
        result['shot_pipeline'] = i[2]
        result['shot_startframe'] = i[3]
        result['shot_endframe'] = i[4]
        result['shot_totaleframe'] = i[5]
        result['shot_descrip'] = i[6]
        jsonData.append(result)
    return jsonData
def getShotTaskInfo(database):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from shottask")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    db.commit()
    db.close()
    jsonData = []
    for i in data:
        result = {}
        result['id'] = i[0]
        result['task_name'] = i[1]
        result['task_descrip'] = i[2]
        result['task_status'] = i[3]
        result['task_user'] = i[4]
        result['task_type'] = i[5]

        jsonData.append(result)
    return jsonData
def getProjectInfo(database):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("select * from project")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    db.commit()
    db.close()
    jsonData = []
    for i in data:
        result = {}
        result['id'] = i[0]
        result['name'] = i[1]
        result['infor'] = i[2]
        result['projectpath'] = i[3]
        result['assetpipeline'] = i[4]
        result['shotpipeline'] = i[5]

        jsonData.append(result)
    return jsonData


def creatAssetInfo(database,dic):
    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    id = dic['id']
    name = dic['name']
    types = dic['types']
    createTime = dic['createTime']
    creator = dic['creator']
    project = dic['project']
    sql = "insert into asset (id,name,type,project,createtime,auther) values ({id},'{name}','{type}','{project}',{createTime},'{creator}')"\
        .format(id=id,name=name,type=types,project=project,createTime = createTime,creator=creator,)
    print(sql)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()
def creatAssetTaskInfo(database,dic):
    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    id = dic['id']
    name = dic['name']
    types = dic['types']
    pipeline = dic['pipeline']
    creator = dic['creator']
    status = dic['status']
    sql = "insert into assettask (id,chinesename,type,pipeline,producer,status) values ({id},'{name}','{type}','{pipeline}','{creator}','{status}')"\
        .format(id=id,name=name,type=types,pipeline=pipeline,creator = creator,status=status)
    print(sql)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()
def creatEpsInfo(database,dic):
    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询

    id = dic['id']
    number = dic['number']
    createTime = dic['createTime']
    creator = dic['creator']
    project = dic['project']
    sql = "insert into eps (id,number,createtime,creator,project) values ({id},'{number}',{createTime},'{creator}','{project}')".format(id=id,number=number,createTime = createTime,creator=creator,project=project)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()
def creatShotInfo(database,dic):
    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询

    id = dic['id']
    shot_name = dic['shot_name']
    shot_pipeline = dic['shot_pipeline']
    shot_startframe = dic['shot_startframe']
    shot_endframe = dic['shot_endframe']
    shot_totalframe = dic['shot_totalframe']
    shot_descrip = dic['shot_descrip']

    sql = "insert into shot (id,shot_name,shot_pipeline,shot_startframe,shot_endframe,shot_totalframe,shot_descrip) values ({id},'{shot_name}','{shot_pipeline}','{shot_startframe}','{shot_endframe}','{shot_totalframe}','{shot_descrip}')".format(id=id,shot_name=shot_name,shot_pipeline = shot_pipeline,shot_startframe=shot_startframe,shot_endframe=shot_endframe,shot_totalframe=shot_totalframe,shot_descrip=shot_descrip)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()
def creatShotTaskInfo(database,dic):
    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询

    id = dic['id']
    task_name = dic['task_name']
    task_descrip = dic['task_descrip']
    task_status = dic['task_status']
    task_user = dic['task_user']
    task_type = dic['task_type']

    sql = "insert into shottask (id,task_name,task_descrip,task_status,task_user,task_type) values ({id},'{task_name}','{task_descrip}','{task_status}','{task_user}','{task_type}')"\
        .format(id=id,task_name=task_name,task_descrip = task_descrip,task_status=task_status,task_user=task_user,task_type=task_type)
    cursor.execute(sql)
    db.commit()
    # 关闭数据库连接
    db.close()
def getDatabeseInfo(database=''):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    sql = "select infor from project"

    # 使用 execute()  方法执行 SQL 查询
    cursor.execute(sql)
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    db.commit()
    # 关闭数据库连接
    db.close()
    return eval(data[0][0])

def DelInfo(database,sql):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    print(cursor.rowcount)
    print('delete success')
    db.close()

def UpDate(database,sql):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root',database)
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def AddProject(newDatabase,infor,modelDatabase):

    allDatabases = getDatabases()
    modelDatabase = modelDatabase
    if newDatabase in allDatabases:
        newDatabase = newDatabase + '_1'
    else:
        newDatabase = newDatabase
    conn = pymysql.connect(host='localhost', user='root', password='root')
    # 创建游标
    cursor = conn.cursor()

    # 创建数据库的sql(如果数据库存在就不创建，防止异常)
    sql = "CREATE DATABASE IF NOT EXISTS {newDatabase};".format(
        newDatabase=newDatabase
    )
    # 执行创建数据库的sql
    cursor.execute(sql)
    sql = "USE {newDatabase};".format(newDatabase=newDatabase)
    cursor.execute(sql)

    sql = "create table project like {modelDatabase}.project;".format(modelDatabase=modelDatabase)
    cursor.execute(sql)
    #初始化project
    id = 1
    infor = infor
    projectpath = getProjectInfo(modelDatabase)[0]['projectpath']
    assetpipeline = getProjectInfo(modelDatabase)[0]['assetpipeline']
    shotpipeline = getProjectInfo(modelDatabase)[0]['shotpipeline']
    sql = 'insert into project (id,name,infor,projectpath,assetpipeline,shotpipeline) values ({id},"{name}","{infor}","{projectpath}","{assetpipeline}","{shotpipeline}")'\
        .format(id=id,name=newDatabase,infor = str(infor),projectpath=projectpath,assetpipeline=assetpipeline,shotpipeline=shotpipeline)
    cursor.execute(sql)

    sql = "create table eps like {modelDatabase}.eps;".format(modelDatabase=modelDatabase)
    cursor.execute(sql)
    sql = "create table asset like {modelDatabase}.asset;".format(modelDatabase=modelDatabase)
    cursor.execute(sql)
    sql = "create table assettask like {modelDatabase}.assettask;".format(modelDatabase=modelDatabase)
    cursor.execute(sql)
    sql = "create table shot like {modelDatabase}.shot;".format(modelDatabase=modelDatabase)
    cursor.execute(sql)
    sql = "create table shottask like {modelDatabase}.shottask;".format(modelDatabase=modelDatabase)
    cursor.execute(sql)

def deleteDatabse(databaseCode):

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "drop database {databaseCode};".format(databaseCode=databaseCode)
    cursor.execute(sql)
    db.commit()
    db.close()


def getUserInfo():

    # 连接database
    db = pymysql.connect('localhost', 'root', 'root','big')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select * from user;"
    cursor.execute(sql)
    data = cursor.fetchall()
    db.commit()
    db.close()
    return data

# print(asdas('1231',{'1':'2'},['q','w'])[0][1])


# data = getDatabases()
# print(data)
# data = getDatabeseInfo(database='big')
# print(data)

#
# asset = getAssetInfo()
# creatAssetInfo()
# print(getAssetInfo('big'),len(getAssetInfo('big')))

# print(getEpsInfo('big')[-1]['id']+1)
# dic = {'id': 17, 'name': '2', 'createTime': 20200428020932, 'creator': '2', 'project': 'big'}
# creatEpsInfo('big',dic)
# DelInfo('big')
# dic = {'id': 2, 'name': 'tree', 'types': 'Props','project': 'big', 'createTime': 20200429063108, 'creator': 'asda'}
# creatAssetInfo('big',dic)
# getAssetInfo('big')
# result = getProjectInfo('big')
# pipeline_dic = eval(result[0]['assetpipeline'])
# print(pipeline_dic)
# print(len(pipeline_dic['asset']))
# dic = eval(getProjectInfo('big')[0]['assetpipeline'])['asset']
# lis = [x for x in dic.keys()]
# print(lis)
# AddProject('newbig')
# print(getProjectInfo('big')[0]['assetpipeline'])
# creatEpsInfo('nihao',{'id': 1, 'name': 'EP001', 'createTime': 20200513051112, 'creator': 'qinjaixin', 'project': 'nihao'})

data = getUserInfo()
for i in data:
    print(i)
