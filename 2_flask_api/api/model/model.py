from db import db

class Model:
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}