# this file structure follows http://flask.pocoo.org/docs/1.0/patterns/appfactories/
# initializing db in api.models.base instead of in api.__init__.py
# to prevent circular dependencies
from .User import User
from .Destination import Destination
from .base import db

__all__ = ["User", "Destination", "db"]
