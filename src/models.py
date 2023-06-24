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
    favorite_character = Column(String(250), nullable = True)
    favorite_planet = Column(String(250), nullable = True)
    

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key =True)
    name = Column(String(250), ForeignKey('User.favorite_character'), ForeignKey('Planet.Character'), unique = True, nullable = False)
    birth_year = Column(Integer, nullable = False)
    homeworld = Column(String(250), nullable = False )

class Planet(Base):
    __tablename__ = 'Planet'
    id = Column(Integer, primary_key = True)
    name = Column(String(250), ForeignKey('user.favorite_planet'), unique = True, nullable = False)
    popluation = Column(Integer, nullable = False)
    climate = Column(String(250), unique = True, nullable = False)

   

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
