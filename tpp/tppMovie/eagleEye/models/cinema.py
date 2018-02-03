# -*- coding:utf-8 -*-
from eagleEye.exts import db, Model, FlagStatus

class Cinema(db.Model, Model):
    __tablename__ = "cinemas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    city = db.Column(db.String(32))
    district = db.Column(db.String(32))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(32))
    score = db.Column(db.Float)
    hallnum = db.Column(db.Integer)
    servicecharge = db.Column(db.Float)
    astrict = db.Column(db.Integer)
    #(business营业、rest休息)
    flag = db.Column(db.Integer, default=FlagStatus.business)
    isDelete = db.Column(db.Boolean, default=False)