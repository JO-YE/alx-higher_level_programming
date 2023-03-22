#!/usr/bin/python3
'''
Prints all City objects from the database hbtn_0e_14_usa
'''
from sqlalchemy import create_engine
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    st_cy = session.query(City, State).filter(City.state_id == State.id).all()\
        .order_by(City.id)

    for city, state in st_cy:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
