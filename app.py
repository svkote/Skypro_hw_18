from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db

from views.movie import movie_ns
from views.genre import genre_ns
from views.director import director_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)

    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)

    with app.app_context():
        db.create_all()

    # create_data(app, db)


# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         with db.session.begin():
#             db.session.add_all


app = create_app(Config())

if __name__ == '__main__':
    # app.run()
    create_app(Config()).run()
