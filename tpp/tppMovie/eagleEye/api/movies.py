# -*- coding:utf-8 -*-
from flask import request, make_response, current_app
from flask.ext.restful import Resource

from eagleEye.models import Movie, HallScheduling

class Movies(Resource):
    def get(self):
        flag = request.args.get("flag")
        limit = request.args.get("limit")
        sort = request.args.get("sort")
        orderby = request.args.get("orderby")
        cinemaID = request.args.get("cinemaID")


        if cinemaID:
            moviesName = {}
            hs = HallScheduling.query.filter(HallScheduling.cinemaID==cinemaID)
            for h in hs:
                movie = Movie.query.get(h.movieID)
                moviesName[str(movie.id)] = movie.showName
            return {"code":200,"data":moviesName}
        else:
            allMoviesArr = Movie.query.filter(Movie.flag == flag)
            if limit:
                allMoviesArr = allMoviesArr.limit(int(limit))
            if sort:
                allMoviesArr=allMoviesArr.order_by(Movie.id)
                if orderby == "desc":
                    allMoviesArr = allMoviesArr.order_by(-Movie.id)

        allMoviesList = []
        for movie in allMoviesArr:
            allMoviesList.append(movie.toDict())
        return {"code":200, "data":allMoviesList}


    def post(self):
        pass
    def delete(self):
        pass
    def put(self):
        pass
    def patch(self):
        pass

