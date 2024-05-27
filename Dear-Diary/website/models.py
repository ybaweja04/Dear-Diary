from . import db
from flask_login import UserMixin
from datetime import datetime

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), unique=True)
    Username = db.Column(db.String(200))
    Password = db.Column(db.String(200))
    notes = db.relationship('Notes')
    