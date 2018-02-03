# -*- coding:utf-8 -*-
from eagleEye.exts.extends import db, api,createOrderID

from eagleEye.exts.flagStatus import FlagStatus


import datetime
class Model():
    # 存储一个对象
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return "success"
        except BaseException as e:
            db.session.rollback()
            return str(e)
    # 存储多个对象
    @classmethod
    def saveAll(cls, arr):
        try:
            db.session.add_all(arr)
            db.session.commit()
            return "success"
        except BaseException as e:
            db.session.rollback()
            return str(e)
    # 存储一个对象
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return "success"
        except BaseException as e:
            db.session.rollback()
            return str(e)
    def toDict(self):
        keys = vars(self).keys()
        obj = {}
        for key in keys:
            if not key.startswith("_"):
                if isinstance(getattr(self, key),datetime.date) or isinstance(getattr(self, key),datetime.time):
                    obj[key] = getattr(self, key).strftime("%Y-%m-%d")
                else:
                    obj[key] = getattr(self, key)
        return obj

