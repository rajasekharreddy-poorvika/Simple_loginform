from flask_sqlalchemy import SQLAlchemy
from flask_login import  UserMixin

db = SQLAlchemy()

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    FirstName = db.Column(db.String(255))
    LastName = db.Column(db.String(252))
    Email = db.Column(db.String(100))
    Doyouownpets = db.Column(db.String(10))
    reason = db.Column(db.String(600))
