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

    state_delete = session.query(State).filter(State.name.like('%a%')).all()

  #  for dele in state_delete:
    session.delete(state_delete)

    session.commit()

    session.close()
