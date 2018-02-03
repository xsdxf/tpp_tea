# -*- coding:utf-8 -*-
import json
import random
import pymysql

db = pymysql.connect("www.sunck.wang", "root", "sunck1999", "movie")
cursor = db.cursor()

def readJsonFile(path):
    with open(path, "rb") as f:
        data = json.load(f)
        return data


arr = readJsonFile("movie2.json")["returnValue"]
screeningModels = ["2D","3D","4D"]

num = 1
for item in arr:
    backgroundPicture = item.get("backgroundPicture")
    if not backgroundPicture:
        backgroundPicture = item.get("poster")
        if not backgroundPicture:
            backgroundPicture = ""
    duration = item.get("duration")
    if duration == None:
        duration = 0
    leadingRole = item.get("leadingRole")
    if not leadingRole:
        leadingRole = "暂无"
    director = item.get("director")
    if not director:
        director = "佚名"
    flag = 2
    if num <= 75:
        flag = 1
    values = str(item["id"])+',"'+item["showName"]+'","'+str(item.get("showNameEn"))+'","'+director+'","'+leadingRole+'","'+item["type"]+'","'+item["country"]+'","'+item["language"]+'",'+str(duration)+',"'+random.choice(screeningModels)+'",date("'+item['openDay']+'"),"'+backgroundPicture+'",'+str(flag)
    insertStr = "insert into movies(id, showname, shownameen, director, leadingRole, type, country, language, duration, screeningmodel, openday, backgroundpicture, flag) values("+ values +");"
    print(insertStr)
    num += 1
    # try:
    #     cursor.execute(insertStr)
    #     db.commit()
    # except:
    #     print("------------------")
    #     db.rollback()


db.close()





