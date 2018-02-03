# -*- coding:utf-8 -*-
from flask import request, make_response, current_app
from flask.ext.restful import Resource

from eagleEye.models import Seat, Hall, HallScheduling, SeatScheduling

class Seats(Resource):
    def get(self):
        # 获取影厅排期id
        hsID = request.args.get("hsID")
        # 查询该影厅排期
        hs = HallScheduling.query.get(hsID)
        # 根据影厅排期查询影厅 得到一个影厅
        hall = Hall.query.get(hs.hallID)
        # 获取该影厅的所有座位
        seatsArr = Seat.query.filter(Seat.hallID==hall.id)

        #获取该影厅排期下的所有座位排期
        ss = SeatScheduling.query.filter(SeatScheduling.hsID==hsID)


        seatsList = []
        for seat in seatsArr:
            for s in ss:
                if s.seatID == seat.id:
                    seat.isAllowSell = False
            seatsList.append(seat.toDict())

        return {"code":200, "count": len(seatsList),"data":seatsList,"movieID":"","cinemaID":"","hallID":"","hsID":""}
    def post(self):
        self.createAllSeats()
        return {"code":201}
        # pass
    def delete(self):
        pass
    def put(self):

        # mlist=list(seat)
        # for i in mlist:
        #     print(i)
        pass
    def patch(self):
        pass

    def createAllSeats(self):
        hallsArr = Hall.query.all()
        for hall in hallsArr:
            for m in range(3):
                for n in range(10):
                    x = m + 1
                    y = n + 1
                    seat = Seat(hall.cinemaID,hall.id,x,x,y)
                    seat.save()

