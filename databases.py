from model import Base, Student


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# replace lecture.db with your own database file
engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()











