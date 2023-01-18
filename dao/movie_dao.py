from model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_one(self, mid: int) -> Movie:
        return self.session.query(Movie).get(mid)

    def get_all_by_director_id(self, did: int) -> list:
        return self.session.query(Movie).filter(Movie.director_id == did).all()

    def get_all_by_genre_id(self, gid: int) -> list:
        return self.session.query(Movie).filter(Movie.genre_id == gid).all()

    def get_all_by_year(self, year: int) -> list:
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, data: dict) -> Movie:
        new_movie = Movie(**data)

        self.session.add(new_movie)
        self.session.commit()

        return new_movie

    def update(self, data: dict) -> Movie or str:
        """Выполняет как полное, так и частичное обновление.
        В словаре на входе обязательно должен быть id"""
        if 'id' not in data:
            return 'Ошибка. Нет ID фильма'
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

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_by_id(self, mid):
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()
