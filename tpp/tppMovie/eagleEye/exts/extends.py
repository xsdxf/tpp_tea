# -*- coding:utf-8 -*-
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_restful import Api
api = Api()

import time, random
def createOrderID():
    strlist = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    orderIDStr = ""
    for i in range(12):
        chr = random.choice(strlist)
        orderIDStr += chr
    tstr = str(time.time())
    orderIDStr = orderIDStr + tstr.split(".")[0] + tstr.split(".")[1]
    return orderIDStr

