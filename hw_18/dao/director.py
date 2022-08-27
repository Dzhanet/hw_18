from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def all_director_movie(self):
        """  Возвращает всех режиссеров"""
        return self.session.query(Director).all()

    def get_one_director(self, director_id):
        """  Возвращает только режиссера по id """
        return self.session.query(Director).get_or_404(director_id)