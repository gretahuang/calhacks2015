from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime
from flask.ext.login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "students"

    ID = db.Column(db.Integer, primary_key=True, unique=True)
    user = db.Column(db.String, unique=True)
    fullname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    reviews = db.relationship('Review', backref='students', lazy='dynamic', foreign_keys=[user_id])

class Review(db.Model):
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    propert = db.Column(db.String)
    landlord = db.Column(Landlord, db.ForeignKey('landlord'))

class Landlord(Base):
    __tablename__ = "landlords"

    fullname = db.Column(db.String)
    is_female = db.Column(db.Boolean, default=True)
    race = db.Column(db.Integer)
    hair_color = db.Column(db.Integer)
    user = db.Column(db.String, primary_key=True)
    total_rate = db.Column(db.Integer, default=0)
    num_rates = db.Column(db.Integer, default=0)
    avg_rating = db.Column(db.Float, default=0.0)
    properties = db.relationship('Review.propert', backref='landlords', lazy='dynamic', primary_key=False, foreign_keys=[landlord])
