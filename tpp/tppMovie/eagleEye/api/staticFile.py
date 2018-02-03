# -*- coding:utf-8 -*-
from flask import request, make_response, current_app

from flask.ext.restful import Resource
class StaticFile(Resource):
    def get(self, filename):
        if not filename:
            filename = "eagleEye/html/index.html"
        elif filename != "favicon.ico":
            filename = "eagleEye/html/" + filename
        response = make_response(current_app.send_static_file(filename))
        return response



