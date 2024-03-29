#!/usr/bin/python3
"""
Contains State class and City relationship
"""
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class State(Base):
    """
    Class with id and name attributes of each state

    __tablename__ (str): The name of the MySQL table to store States
    id (sqlalchemy.Integer): The state's id
    name (sqlalchemy.String): The state's name
    cities (sqlalchemy.orm.relationship): The State-City relationship
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
