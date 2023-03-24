#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from relationship_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    st = session.query(State).order_by(State.id)

    for state in st:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
