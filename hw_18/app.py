from flask import Flask
from flask_restx import Api

from api.directores import director_ns
from api.genres import genre_ns
from api.movies import movies_ns
from config import Config
from setup_db import db
from views_error.views_error import page_error


def create_app(config_object):
    """  Функция создает основной объект app """
    app = Flask(__name__)
    app.register_blueprint(page_error)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """ Функция подключает Flask-SQLAlchemy, Flask-RESTx"""
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app(Config())
    app.run()
