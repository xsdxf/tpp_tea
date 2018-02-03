# -*- coding:utf-8 -*-
from flask import request, make_response, current_app
from flask.ext.restful import Resource

from eagleEye.models import Hall, Cinema, Movie, HallScheduling

import random

class HallSchedulings(Resource):
    def get(self):
        cinemaID = request.args.get("cinemaID")
        movieID  = request.args.get("movieID")
        playDate = request.args.get("playDate")

        hallSchedulingsArr = HallScheduling.query.filter(HallScheduling.cinemaID==cinemaID,HallScheduling.movieID==movieID)

        hallSchedulingsList = []
        for hallScheduling in hallSchedulingsArr:
            hallSchedulingsList.append(hallScheduling.toDict())
        return {"code":200, "data":hallSchedulingsList,'length':len(hallSchedulingsList)}


    def post(self):
        self.createAllHallSchedulings()
        return {"code":201}
        # pass
    def delete(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass

    def createAllHallSchedulings(self):
        # 所有影院
        cinemasArr = Cinema.query.all()
        hallNamesArr = ["北京", "上海", "广州", "深圳", "天津"]
        screenTypesArr = ["高清", "普通", "超清"]
        soundTypesArr = ["杜比", "环绕", "普通"]
        for cinema in cinemasArr:
            # 创建影厅
            for i in range(5):
                hall = Hall(cinema.id, hallNamesArr[i], random.choice(screenTypesArr), random.choice(screenTypesArr),
                            30)
                hall.save()
                # 为影院设置排期
                # 取出正在热映的5部电影
                playMoviesArr = Movie.query.filter(Movie.flag == 1)
                playMoviesArr = list(playMoviesArr)
                playMoviesNum = len(playMoviesArr)
                startTimesArr = ["2018-02-02 06:00:00", "2018-02-02 09:00:00", "2018-02-02 12:00:00",
                                 "2018-02-02 15:00:00", "2018-02-02 18:00:00"]
                for j in range(5):
                    # 随机拿出一个热映下标
                    index = random.choice(range(playMoviesNum))
                    movie = playMoviesArr[index]
                    hallScheduling = HallScheduling(movie.id, cinema.id, hall.id, 100, 50, startTimesArr[j],
                                                    movie.duration + 20)
                    hallScheduling.save()