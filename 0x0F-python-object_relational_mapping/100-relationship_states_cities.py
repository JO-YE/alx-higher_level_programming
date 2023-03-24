#!/usr/bin/python3
"""
Creates the State "California" with the City San Francisco
"""
from sqlalchemy import create_engine
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(State(name="California", cities=[City(name="San Francisco")]))
    session.commit()
