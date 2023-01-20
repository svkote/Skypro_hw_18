from .model.director import Director


class DirectorDao:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_one(self, did: int) -> Director:
        return self.session.query(Director).get(did)
