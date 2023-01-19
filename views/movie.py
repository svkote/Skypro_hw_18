from flask import request
from flask_restx import Namespace, Resource

from implemented import movies_schema, movie_schema, movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        data = {
            'director': request.args.get('director_id'),
            'genre': request.args.get('genre_id'),
            'year': request.args.get('year')
        }
        all_movies = movie_service.filters(data)
        return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        new_movie = movie_service.create(data)
        return '', 201, {'location': f'/movies/{new_movie.id}'}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        data['id'] = mid
        movie_service.update(data)

        return 'ok', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return 'ok', 204

