# -*- coding:utf-8 -*-
from flask import request, make_response, current_app
from flask.ext.restful import Resource

from eagleEye.models import Cinema

class Cinemas(Resource):
    def get(self):
        city = request.args.get("city")
        district = request.args.get("area")
        page  = request.args.get("page")
        count = request.args.get("count")

        cinemasArr = Cinema.query.filter(Cinema.city==city)
        print('-----',cinemasArr,type(cinemasArr))
        if district:
            cinemasArr = cinemasArr.filter(Cinema.district==district)
        if page:
            page = int(page)
            count = int(count)
            cinemasArr = cinemasArr.offset((page-1)*count).limit(count)
            # cinemasArr = cinemasArr.offset((page-1)*count)

        cinemasList = []
        for cinema in cinemasArr:
            cinemasList.append(cinema.toDict())
        # return 'ok'
        return {"code":201 ,"data":cinemasList,'length':len(cinemasList)}


    def post(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass

