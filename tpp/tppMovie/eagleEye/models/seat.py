# -*- coding:utf-8 -*-
from eagleEye.exts import db, Model

class Seat(db.Model, Model):
    __tablename__ = "seats"
    id = db.Column(db.Integer, primary_key=True)
    cinemaID = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallID = db.Column(db.Integer, db.ForeignKey("halls.id"))
    # 1普通 2沙发 3床
    seatType = db.Column(db.Integer)
    x = db.Column(db.Integer)
    y = db.Column(db.Integer)
    isAllowSell = db.Column(db.Boolean, default=True)
    # (0损坏、1正常)
    flag = db.Column(db.Integer, default=1)
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self,cinemaID,hallID,seatType,x,y):
        self.cinemaID =cinemaID
        self.hallID =hallID
        self.seatType =seatType
        self.x =x
        self.y =y
