from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    data_created = db.Column(db.DateTime(timezone=True), default=func.now())

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    key = db.Column(db.String(300), unique=True)
    content = db.Column(db.String(100000000))
    date_posted = db.Column(db.DateTime(timezone=True), default=func.now())
