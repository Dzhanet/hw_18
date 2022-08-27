import json

from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movies_ns = Namespace('movies')


@movies_ns.route("/")
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)
        filters = {
            "director_id": director_id,
            "genre_id": genre_id,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(all_movies)
        return result, 200

    def post(self):
        req_json = json.loads(request.data)
        add_movie = movie_service.create(req_json)
        return f"Фильм {add_movie.title} добавлен ", 201, {"location": f"/movies/{add_movie.id}"}


@movies_ns.route("/<int:pk>")
class MoviesView(Resource):
    def get(self, pk):
        one_movie = movie_service.get_one(pk)
        one = MovieSchema().dump(one_movie)
        return one, 200

    def put(self, pk):
        movie_service.update(pk)
        return "", 204

    def delete(self, pk):
        movie_service.delete(pk)
        return "", 204
