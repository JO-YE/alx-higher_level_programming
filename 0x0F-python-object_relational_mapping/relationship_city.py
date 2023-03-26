#!/usr/bin/python3
"""
Defines a City class
Inherits from SQLAlchemy Base and links to the MySQL table cities
"""
from sqlalchemy import Integer, ForeignKey, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class with id, name, and state_id attributes for each city.

     __tablename__ (str): The name of the MySQL table to store Cities.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id(sqlalchemy.Integer): Foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
