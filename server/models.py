from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model, SerializerMixin):
    __tablename__ = 'earthquakes'

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __init__(self, magnitude=None, location=None, year=None):
        self.magnitude = magnitude
        self.location = location
        self.year = year
