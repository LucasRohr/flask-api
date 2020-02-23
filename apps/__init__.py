from flask import Flask
from config import config
from .api import configure_api
from .db import db


def create_app(config_name):
    app = Flask('api-users')

    app.config.from_object(config[config_name])

    db.init_app(app)

    configure_api(app)

    return app
