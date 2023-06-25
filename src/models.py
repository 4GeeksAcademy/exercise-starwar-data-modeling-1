import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key= True)
    username = Column(String(250), unique = True, nullable = False)
    password = Column(String(250), nullable = False)
    favorite_character = relationship('Character', backref = 'User', uselist = False)
    favorite_planet = relationship('Planet', backref = 'User', uselist = False)
    

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key =True)
    name = Column(String(250), ForeignKey('User.favorite_character'), ForeignKey('Planet.Character'), unique = True, nullable = False)
    birth_year = Column(Integer, nullable = False)
    homeworld = Column(String(250), nullable = False )

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), ForeignKey('User.favorite_planet'), unique = True, nullable = False)
    popluation = Column(Integer, nullable = False)
    climate = Column(String(250), unique = True, nullable = False)

class Favorite(Base):
    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    Favorite_id = Column(Integer, ForeignKey("User"))

   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
