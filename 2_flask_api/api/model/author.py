from model.model import Model
from db import db

class Author(db.Model, Model):
    __tablename__ = 'author'

    id = db.Column(db.Integer, db.Sequence('seq_author_id'), primary_key=True)
    name = db.Column(db.String)
    
    musics = db.relationship('Music', backref='author', lazy=True)

    def __init__(self, name):
        self.name = name
