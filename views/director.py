from flask_restx import Namespace, Resource

from implemented import directors_schema, director_schema, director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200


@director_ns.route('/<int:did>/')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200
