# -*- coding:utf-8 -*-
from flask import Blueprint
urls = Blueprint("eagleEye", "urls")


from eagleEye.exts import api
from eagleEye.api.staticFile import StaticFile

from eagleEye.api.movies import Movies
from eagleEye.api.cinemas import Cinemas
from eagleEye.api.halls import Halls
from eagleEye.api.hallschedulings import HallSchedulings
from eagleEye.api.seats import Seats
from eagleEye.api.orders import Orders

api.add_resource(Movies, "/movies")
api.add_resource(Cinemas, "/cinemas")
api.add_resource(Halls, "/halls")
api.add_resource(HallSchedulings, "/hallschedulings")
api.add_resource(Seats, "/seats")
api.add_resource(Orders, "/orders")

api.add_resource(StaticFile, "/<regex('.*'):filename>")