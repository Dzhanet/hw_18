import json

from flask import request

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_alL_movies(self):
        """ Возвращает список всех фильмов, разделенный по страницам """
        return self.session.query(Movie).limit(5).offset(5).all()

    def get_one_movie(self, pk):
        """ Возвращает подробную информацию о фильме. """
        return self.session.query(Movie).get_or_404(pk)

    def get_movie_by_director(self, director_id):
        """ Возвращает все фильмы режиссера """
        return self.session.query(Movie).filter(Director.id == director_id).join(Movie.director).all()

    def get_movie_by_genre(self, genre_id):
        """ Возвращает все фильмы жанра """
        return self.session.query(Movie).filter(Genre.id == genre_id).join(Movie.genre).all()

    def get_movie_by_year(self, year):
        """ Возвращает все фильмы за год """
        return self.session.query(Movie).filter(Movie.year == year).all()

    def add_movies(self, movie):
        """ Добавляет фильм методом POST """
        new_movies = Movie(**movie)
        self.session.add(new_movies)
        self.session.commit()
        return new_movies

    def update_movie(self, pk):
        """ Обновляет данные о фильме методом PUT """
        movie = json.loads(request.data)
        updates_movie = self.session.query(Movie).filter(Movie.id == pk)
        updates_movie.update(movie)
        self.session.commit()

    def delete_movie(self, pk):
        """ Удаляет данные о фильме """
        movie = self.get_one_movie(pk)
        self.session.delete(movie)
        self.session.commit()
