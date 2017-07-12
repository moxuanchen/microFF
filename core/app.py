# -*- coding: utf-8 -*-

from flask import Flask
from api.api import api
from core.database import db
from views.views import blueprint
from settings import get_config_env


def create_app(config=get_config_env()):
    app = Flask(__name__)
    app.config.from_object(config)
    api.init_app(app)
    db.init_app(app)
    app.register_blueprint(blueprint)
    return app
