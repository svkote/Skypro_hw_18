from flask_restx import Namespace, Resource

from implemented import genres_schema, genre_schema, genre_service

genre_ns = Namespace('directors')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre), 200
