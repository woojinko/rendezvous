from api.core import Mixin
from .base import db

# Note that we use sqlite for our tests, so you can't use Postgres Arrays
class User(Mixin, db.Model):
    """User Table."""

    __tablename__ = "user"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    code = db.Column(db.Integer, nullable=False)

    def __init__(self, lat, lon, code):
        db.Model.__init__(self, lat=lat, lon=lon, code=code)

    def add_user(self):
        db.session.add(self)
        db.session.commit()
