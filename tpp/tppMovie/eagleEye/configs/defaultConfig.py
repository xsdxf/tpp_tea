# -*- coding:utf-8 -*-
class DefaultConfig():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:rock1204@127.0.0.1:3306/tpp0202"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "sunck"


from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    def __init__(self, url, *args):
        super(RegexConverter, self).__init__(url)
        self.regex = args[0]



