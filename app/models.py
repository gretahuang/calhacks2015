from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime
from flask.ext.login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "students"

    ID = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String, unique=True)
    fullname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    reviews = db.relationship('Review', backref='students', lazy='dynamic', foreign_keys=[user_id])

class Landlord(db.Model):
    __tablename__ = "landlords"

    landlord_id = db.Column(db.Integer, primary_key=True, unique=True)
    fullname = db.Column(db.String)
    username = db.Column(db.String)
    is_female = db.Column(db.Boolean, default=True)
    race = db.Column(db.Integer)
    hair_color = db.Column(db.Integer)
    total_rate = db.Column(db.Integer, default=0)
    num_rates = db.Column(db.Integer, default=0)
    avg_rating = db.Column(db.Float, default=0.0)
    landlord = db.Column(db.String, ForeignKey('landlord'))
    properties = db.relationship('Review.propert', backref='landlords', lazy='dynamic', foreign_keys=[landlord]) #Review.propert? how to get attr not object

class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime)
    body = db.Column(db.String(140))
    propert = db.Column(db.String)
    landlord = db.Column('Landlord') #quotes?