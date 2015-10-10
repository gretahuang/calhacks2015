from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from app import models
from sqlalchemy.orm import sessionmaker

Base = declarative_base
engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

print(models.User.__table__)
testu = models.User(fullname='test', email='test')
session.add(testu)
our_user = session.query(models.User).filter_by(fullname='test').first()
print(our_user)