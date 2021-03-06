from flask import Flask
from os import getenv

from app.configs import database, migrations, jwt, scheduler
from app import routes


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = getenv("SECRET_KEY")
    app.config['JSON_SORT_KEYS'] = False

    database.init_app(app)
    migrations.init_app(app)
    jwt.init_app(app)
    scheduler.init()
    routes.init_app(app)

    return app
