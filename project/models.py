from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	username = db.Column(db.String(1000))
	biography = db.Column(db.String(1000))


class Posts(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy

	post = db.Column(db.String(512),nullable=False)
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

