from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Students(Base):
  __tablename__ = 'students'
   student_id = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(Integer)
   picture = Column(String)
   description = Column(String)


class Cart(Base):
   __tablename__ = 'cart'
   cart_id = Column(Integer, primary_key=True)

