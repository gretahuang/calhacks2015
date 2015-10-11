from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime
from flask.ext.login import UserMixin

USERNAME_LEN = 20
FULLNAME_LEN = 40
EMAIL_LEN = 30
BODY_LEN = 2000

class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(USERNAME_LEN), unique=True)
    fullname = db.Column(db.String(FULLNAME_LEN))
    email = db.Column(db.String(EMAIL_LEN), unique=True)

    # HAS MANY: reviews
    reviews = db.relationship('Review', backref='users', lazy='dynamic')

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    timestamp = db.Column(db.DateTime)
    body = db.Column(db.String(BODY_LEN))

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    landlord_id = db.Column(db.Integer, db.ForeignKey('landlords.id'))

class Landlord(db.Model):
    __tablename__ = "landlords"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    fullname = db.Column(db.String(FULLNAME_LEN))
    username = db.Column(db.String(USERNAME_LEN))
    is_female = db.Column(db.Boolean, default=True)
    race = db.Column(db.Integer)
    hair_color = db.Column(db.Integer)
    total_rate = db.Column(db.Integer, default=0)
    num_rates = db.Column(db.Integer, default=0)
    avg_rating = db.Column(db.Float, default=0.0)

    # HAS MANY: properties, reviews
    properties = db.relationship(LLProperty, backref='landlords', lazy='dynamic')
    reviews = db.relationship('Review', backref='landlords', lazy='dynamic')

class LLProperty(db.Model):
    __tablename__ = "properties"
    id = db.Column(db.Integer, primary_key=True, unique=True)

    # foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('landlords.id'))
    review_id  = db.Column(db.Integer, db.ForeignKey('reviews.id'))
