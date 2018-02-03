# -*- coding:utf-8 -*-
import json
import pymysql

def readJsonFile(path):
    with open(path, "rb") as f:
        data = json.load(f)
        return data


arr = readJsonFile("city.json")


# db = pymysql.connect("www.sunck.wang", "root", "sunck1999", "movie")
# cursor = db.cursor()

# for item in arr:
#     print(item)
#     break



