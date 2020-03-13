import datetime
import jwt
from .. import db, flask_bcrypt
from ..config import key
from app.main.model.blacklist import BlacklistToken


class Movie(db.Model):
    """ Movie Model for storing movie related details """
    __tablename__ = "movie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(512),  nullable=False)
    imdb_title = db.Column(db.String(512), )
    catalogue_entry = db.Column(db.String(64), nullable=False)
    rating = db.Column(db.Float())
    cover = db.Column(db.String(1024))
    registered_on = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Movie '{}'>".format(self.moviename)
