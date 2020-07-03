from model.model import Model
from db import db

class Music(db.Model, Model):
    __tablename__ = 'music'

    id = db.Column(db.Integer, db.Sequence('seq_music_id'), primary_key=True)
    name = db.Column(db.String)
    
    authorId = db.Column(db.Integer, db.ForeignKey('author.id'), index=True, nullable=False)

    def __init__(self, name, authorId):
        self.name = name
        self.authorId = authorId
