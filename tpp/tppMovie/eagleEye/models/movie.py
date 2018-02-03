# -*- coding:utf-8 -*-
from eagleEye.exts import db, Model


class Movie(db.Model, Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    showName = db.Column(db.String(64))
    showNameEN = db.Column(db.String(64))
    director = db.Column(db.String(32))
    leadingRole = db.Column(db.String(256))
    type = db.Column(db.String(64))
    country = db.Column(db.String(32))
    language = db.Column(db.String(32))
    duration = db.Column(db.Integer)
    screeningModel = db.Column(db.String(16))
    openDay = db.Column(db.Date)
    backgroundPicture = db.Column(db.String(256))
    # (hotingShow热映 prepareShow即将上映)
    flag = db.Column(db.Integer)
    isDelete = db.Column(db.Boolean, default=False)



