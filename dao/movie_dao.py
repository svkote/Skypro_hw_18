from .model.movie import Movie


class MovieDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        all_movie = self.session.query(Movie).all()
        return all_movie

    def get_one(self, mid: int) -> Movie:
        return self.session.query(Movie).get(mid)

    def get_all_for_filter(self):
        return self.session.query(Movie)

    def filter_all_by_director_id(self, all_movies, did: int):
        return all_movies.filter(Movie.director_id == did)

    def filter_all_by_genre_id(self, all_movies, gid: int):
        return all_movies.filter(Movie.genre_id == gid)

    def filter_all_by_year(self, all_movies, year: int):
        return all_movies.filter(Movie.year == year)

    def final_filter(self, all_movies):
        return all_movies.all()

    def create(self, data) -> Movie:
        new_movie = Movie(**data)

        # self.session.add(new_movie)
        # self.session.commit()
        #
        # return new_movie
        return self.update(new_movie)

    def update(self, movie) -> Movie or str:
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete_by_id(self, movie):
        self.session.delete(movie)
        self.session.commit()
