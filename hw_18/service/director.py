from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.all_director_movie()

    def get_one(self, director_id):
        return self.dao.get_one_director(director_id)
