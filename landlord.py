from sqlalchemy import *

class Landlord:
    __tablename__ = "landlord"
    name = Column(String, primary_key=False)
    user = Column(string, primary_key=True)
    proprties = Column(postgresql.ARRAY(String), primary_key=False)

    def __init__(self, name, propert, user=None):
        self.name = name
        self.user = user
        self.properties = propert
        self.total_rate = 0
        self.avg_rate = None
        self.num_rates = 0

    def update_rating(rating):
        self.total_rate += rating
        self.num_rates += 1
        self.avg_rate = self.total_rate/self.num_rates






