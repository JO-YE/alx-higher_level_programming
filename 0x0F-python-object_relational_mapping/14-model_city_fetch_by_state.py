#!/usr/bin/python3
'''
A python file that prints all City objects from database
'''
from sqlalchemy import create_engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st_cy = session.query(State, City).filter(City.state_id == State.id).all()

    for state, city in st_cy:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
