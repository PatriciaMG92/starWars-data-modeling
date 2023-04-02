import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    name= Column(String(250), nullable=False)
    description = Column(String(250), nullable = False)
    gender = Column(String(250))
    height = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    favorites = Column(Integer, ForeignKey('favorites.id'))


class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    image_url = Column(String(250), nullable=False)
    name= Column(String(250), nullable=False)
    description = Column(String(250), nullable = False)
    climate = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)
    terrain = Column(String(250))
    surface_water = Column(Integer)
    orbital_period = Column(Integer)
    favorite = Column(Integer, ForeignKey('favorites.id'))
   

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
