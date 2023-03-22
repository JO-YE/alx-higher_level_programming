#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Integer, Table, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    '''  Represents a city column for a MySQL table

    __tablename__ (str): The name of the MySQL table to store Cities.
    id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    state_id(sqlalchemy.Integer): Foreign key to states.id
    '''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
