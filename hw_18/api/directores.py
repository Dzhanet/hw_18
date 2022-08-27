from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        alL_directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(alL_directors)
        return result, 200


@director_ns.route('/<int:pk>')
class DirectorView(Resource):
    def get(self, pk):
        one_director = director_service.get_one(pk)
        result = DirectorSchema().dump(one_director)
        return result, 200
