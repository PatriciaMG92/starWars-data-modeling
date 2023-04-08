import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    username= Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    characters_favorites_id = Column(Integer, ForeignKey('favorites_characters_id'))
    planets_favorites_id = Column(Integer, ForeignKey('favorites_planets_id'))

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


class Favorites_characters(Base):
    __tablename__ = 'favorites_characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planets_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
 

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
