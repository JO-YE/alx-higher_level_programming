#!/usr/bin/python3
'''
a python file that contains the class definition of a State
and an instance Base = declarative_base()
'''
from sqlalchemy import create_engine
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_statename = State(name='Louisiana')
    session.add(new_statename)
    session.commit()

    print(new_statename.id)
    session.close()
