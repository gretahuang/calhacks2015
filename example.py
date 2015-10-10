from sqlalchemy import *

class Student:
    __tablename__ = "student"
    name = Column(String, primary_key=False)
    user = Column(String, primary_key=True)
    proprties = Column(postgresql.ARRAY(String), primary_key=False)
    reviews = Column(postgresql.ARRAY(Review), primary_key=False)

    def __init__(self, name):
        self.name = name
        self.user = user

    def review(self, landlord, rating):
        landlord.update_rating(rating)
        review = Review(self, landlord_name, rating)


