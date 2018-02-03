# -*- coding:utf-8 -*-
from eagleEye.exts import db, Model

from sqlalchemy import text

class SeatScheduling(db.Model, Model):
    __tablename__ = "seatschedulings"
    id = db.Column(db.Integer, primary_key=True)
    cinemaID = db.Column(db.Integer, db.ForeignKey("cinemas.id"))
    hallID = db.Column(db.Integer, db.ForeignKey("halls.id"))
    seatID = db.Column(db.Integer, db.ForeignKey("seats.id"))
    hsID = db.Column(db.Integer, db.ForeignKey("hallschedulings.id"))
    orderID = db.Column(db.String(128), db.ForeignKey("orders.orderID"))
    createTime = db.Column(db.TIMESTAMP(True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    def __init__(self,cinemaID,hallID,seatID,hsID,orderID):
        self.cinemaID =cinemaID
        self.hallID =hallID
        self.seatID =seatID
        self.hsID =hsID
        self.orderID =orderID
