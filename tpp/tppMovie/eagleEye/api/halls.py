# -*- coding:utf-8 -*-
from flask import request, make_response, current_app
from flask.ext.restful import Resource

from eagleEye.models import Hall

class Halls(Resource):
    def get(self):
        return "halls"
    def post(self):
        cinemaID = request.form.get("cinemaID")
        name = request.form.get("name")
        screenType = request.form.get("screenType")
        scoundType = request.form.get("scoundType")
        seatNum = request.form.get("seatNum")

        hall = Hall(cinemaID,name,screenType,scoundType,seatNum)
        hall.save()
        return {"code":201, "hall":hall.toDict()}

    def delete(self):
        hallID = request.form.get("hallID")
        hall = Hall.query.get(hallID)
        hall.delete()
        return {"code":204}
    def put(self):
        pass
    def patch(self):
        hallID = request.form.get("id")
        name = request.form.get("name")
        hall = Hall.query.get(hallID)
        hall.name = name
        hall.save()
        return {"code": 201, "hall": hall.toDict()}

