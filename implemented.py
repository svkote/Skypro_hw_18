from dao.movie_dao import MovieDao
from dao.genre_dao import GenreDao
from dao.director_dao import DirectorDao

from service.director_service import DirectorService
from service.genre_service import GenreService
from service.movie_service import MovieService

from dao.model.movie import MovieSchema
from dao.model.genre import GenreSchema
from dao.model.director import DirectorSchema

from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieService(dao=movie_dao)
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

genre_dao = GenreDao(db.session)
genre_service = GenreService(dao=genre_dao)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

director_dao = DirectorDao(db.session)
director_service = DirectorService(dao=director_dao)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
