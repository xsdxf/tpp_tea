# -*- coding:utf-8 -*-
from flask import request, make_response, current_app
from flask.ext.restful import Resource

from eagleEye.models import Order, SeatScheduling
from eagleEye.exts import createOrderID

class Orders(Resource):
    def get(self):
        pass
    def post(self):
        movieID = int(request.form.get("movieID"))
        cinemaID = int(request.form.get("cinemaID"))
        hallID = int(request.form.get("hallID"))
        hsID = int(request.form.get("hsID"))
        seatsList = request.form.getlist("seatID")
        piaoNum = int(request.form.get("piaoNum"))
        piaoPrice = float(request.form.get("piaoPrice"))




        #生成一个订单号
        orderIdStr = createOrderID()

        order = Order(orderIdStr, movieID, cinemaID, hallID, hsID, ",".join(seatsList), "", piaoNum,piaoPrice)
        order.save()

        ssIdList = []
        for seatID in seatsList:
            seatID = int(seatID)
            ss = SeatScheduling(cinemaID, hallID, seatID, hsID, orderIdStr)
            ss.save()
            ssIdList.append(str(ss.id))
        order.ssIDStr = ",".join(ssIdList)

        #创建取票码
        qupiaoStr = orderIdStr[:10]
        order.qupiaoStr = qupiaoStr
        order.save()

        return {"code":201, "data":order.toDict()}
        # return 'order'

    def delete(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass

