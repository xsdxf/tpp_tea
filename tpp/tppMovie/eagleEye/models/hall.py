# -*- coding:utf-8 -*-
from eagleEye.exts import db, Model, FlagStatus

class Hall(db.Model, Model):
    __tablename__ = "halls"
    id = db.Column(db.Integer, primary_key=True)
    cinemaID = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    name = db.Column(db.String(32))
    # 普通、高清、超清
    screenType = db.Column(db.String(16))
    # 普通、环绕、杜比
    soundType = db.Column(db.String(16))
    seatNum = db.Column(db.Integer)
    # (close关闭、dispark开放)
    flag = db.Column(db.Integer, default=FlagStatus.dispark)
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self,cinemaID,name,screenType,soundType,seatNum):
        self.cinemaID =cinemaID
        self.name =name
        self.screenType =screenType
        self.soundType =soundType
        self.seatNum =seatNum
