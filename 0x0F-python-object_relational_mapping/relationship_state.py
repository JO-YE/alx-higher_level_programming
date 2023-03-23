#!/usr/bin/python3
''' Continuation from model_state with a new attribute and
    relationship function linking State with Class City
'''
from sqlalchemy import Integer, Table, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''
    Class with id and name attributes of each state
    '''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all', 'delete')
