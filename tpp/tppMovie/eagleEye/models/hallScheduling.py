# -*- coding:utf-8 -*-
from eagleEye.exts import db, Model, FlagStatus

from sqlalchemy import text
from sqlalchemy.sql import func

class HallScheduling(db.Model, Model):
    __tablename__ = "hallschedulings"
    id = db.Column(db.Integer, primary_key=True)
    movieID = db.Column(db.Integer, db.ForeignKey("movies.id"))
    cinemaID = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallID = db.Column(db.Integer, db.ForeignKey("halls.id"))
    # originalPrice原价 price售价
    pressType = db.Column(db.Integer, default=FlagStatus.price)
    originalPrice = db.Column(db.Float)
    price = db.Column(db.Float)
    startTime = db.Column(db.Time)
    duration = db.Column(db.Integer)
    createTime = db.Column(db.TIMESTAMP(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    lastTime = db.Column(db.Time, onupdate=func.now())
    #notShow未放映、showing正在放映、endShow结束放映
    flag = db.Column(db.Integer, default=FlagStatus.notShow)
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self,movieID,cinemaID,hallID,originalPrice,price,startTime,duration):
        self.movieID=movieID
        self.cinemaID=cinemaID
        self.hallID =hallID
        self.originalPrice =originalPrice
        self.price =price
        self.startTime =startTime
        self.duration =duration
