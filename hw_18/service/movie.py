from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_movie_by_director(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_movie_by_genre(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_movie_by_year(filters.get("year"))
        else:
            movies = self.dao.get_alL_movies()
        return movies

    def get_one(self, pk):
        return self.dao.get_one_movie(pk)

    def create(self, movie):
        return self.dao.add_movies(movie)

    def update(self, pk):
        return self.dao.update_movie(pk)

    def delete(self, pk):
        self.dao.delete_movie(pk)
