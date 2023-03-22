#!/usr/bin/python3
'''
A python file that contains the class definition of a City
and an instance Base = declarative_base() from model_state
'''
from sqlalchemy import Integer, Table, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    '''
    Class with id and name, state_id attributes of each state
    '''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
