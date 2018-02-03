# -*- coding:utf-8 -*-
from flask import Flask

from eagleEye.configs import RegexConverter, DevelopmentConfig, TestingConfig, ProductionConfig
from eagleEye.exts import db, api
from eagleEye.api import urls

def create_app():
    # 创建app对象
    app = Flask("ttpMovie")

    # 加载配置
    app.config.from_object(DevelopmentConfig)
    # 注册转换器类
    app.url_map.converters["regex"] = RegexConverter

    # 三方对象加载app对象
    db.init_app(app)
    api.init_app(app)

    # 注册路由
    app.register_blueprint(urls)
    return app