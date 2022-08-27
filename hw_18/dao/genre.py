from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def all_genre_movie(self):
        """  Возвращает все жанры """
        return self.session.query(Genre).all()

    def get_one_genre(self, genre_id):
        """  Возвращает только жанр по id """
        return self.session.query(Genre).get_or_404(genre_id)