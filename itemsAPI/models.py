from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from .database import Base



""" Model for the User to maipulate the user table in database"""

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    email = Column(String(200), unique=True, index=True, nullable=False)
    password = Column(String(200), nullable=False)




""" Model for the User to maipulate the user table in database"""

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String(200), nullable=False)
    item_location = Column(String(300), nullable=False)
    item_description = Column(String(300), nullable=False)
    item_date = Column(Date, nullable=False)