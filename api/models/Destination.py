from api.core import Mixin
from .base import db

# Note that we use sqlite for our tests, so you can't use Postgres Arrays
class Destination(Mixin, db.Model):
    """Destination Table."""

    __tablename__ = "destination"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    code = db.Column(db.Integer)

    def __init__(self, lat, lon, code):
        db.Model.__init__(self, lat=lat, lon=lon, code=code)

    def add_dest(self):
        db.session.add(self)
        db.session.commit()
