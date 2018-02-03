# -*- coding:utf-8 -*-
from eagleEye.exts import db, Model, FlagStatus

from sqlalchemy import text
from sqlalchemy.sql import func


class Order(db.Model, Model):
    __tablename__ = "orders"
    orderID = db.Column(db.String(128), primary_key=True)
    movieID = db.Column(db.Integer, db.ForeignKey("movies.id"))
    cinemaID = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallID = db.Column(db.Integer, db.ForeignKey("halls.id"))
    hsID = db.Column(db.Integer, db.ForeignKey("hallschedulings.id"))
    #"1,2,3,4,5,6"
    seatIDStr = db.Column(db.String(128))
    #"1,2,3,4,5,6"
    ssIDStr = db.Column(db.String(128))

    qupiaoStr = db.Column(db.String(32))
    piaoNum = db.Column(db.Integer)
    piaoPrice = db.Column(db.Float)

    createTime = db.Column(db.TIMESTAMP(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    payTime = db.Column(db.Time)
    getTime = db.Column(db.Time)
    tuikuanTime = db.Column(db.Time)
    lastTime = db.Column(db.Time, onupdate=func.now())
    #(notPay未支付、payNotTicket已支付未取票、payAndTicket已支付已取票、refundTicket退票)
    flag = db.Column(db.Integer, default=FlagStatus.notPay)
    isDelete = db.Column(db.Boolean, default=False)
    def __init__(self,orderID,movieID,cinemaID,hallID,hsID,seatIDStr,ssIDStr,piaoNum,piaoPrice):
        self.orderID =orderID
        self.movieID =movieID
        self.cinemaID =cinemaID
        self.hallID =hallID
        self.hsID =hsID
        self.seatIDStr =seatIDStr
        self.ssIDStr =ssIDStr
        self.piaoNum =piaoNum
        self.piaoPrice =piaoPrice
