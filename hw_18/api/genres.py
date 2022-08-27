from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        all_genre = genre_service.get_all()
        result = GenreSchema(many=True).dump(all_genre)
        return result, 200


@genre_ns.route('/<int:pk>')
class GenreView(Resource):
    def get(self, pk):
        one_genre = genre_service.get_one(pk)
        result = GenreSchema().dump(one_genre)
        return result, 200
