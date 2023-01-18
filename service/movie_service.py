from dao.movie_dao import MovieDao


class MovieService:
    def __init__(self, dao: MovieDao):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, mid: int):
        return self.dao.get_one(mid)

    def filters(self, data):
        """Не уверена, что это делается так"""
        all_movies = self.dao.get_all_for_filter()

        if data['director_id']:
            all_movies = self.dao.filter_all_by_director_id(all_movies, data['director_id'])
        if data['genre_id']:
            all_movies = self.dao.filter_all_by_genre_id(all_movies, data['genre_id'])
        if data['year']:
            all_movies = self.dao.filter_all_by_year(all_movies, data['year'])

        return self.dao.final_filter(all_movies)

    def create(self, data: dict):
        return self.dao.create(data)

    def update(self, data: dict):
        """Выполняет как полное, так и частичное обновление.
        В словаре на входе обязательно должен быть id"""
        if 'id' not in data:
            return self.dao.create(data)

        mid = data['id']

        movie = self.get_one(mid)

        if 'title' in data:
            movie.title = data['title']
        if 'description' in data:
            movie.description = data['description']
        if 'trailer' in data:
            movie.trailer = data['trailer']
        if 'year' in data:
            movie.year = data['year']
        if 'rating' in data:
            movie.rating = data['rating']
        if 'genre_id' in data:
            movie.genre_id = data['genre_id']
        if 'director_id' in data:
            movie.director_id = data['director_id']

        return self.dao.update(movie)

    def delete(self, mid: int):
        movie = self.get_one(mid)
        self.dao.delete_by_id(movie)
