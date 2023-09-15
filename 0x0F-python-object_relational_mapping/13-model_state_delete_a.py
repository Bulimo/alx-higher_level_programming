#!/usr/bin/python3
"""
Module 13-model_state_delete_a
deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    del_state = my_session.query(State).filter(State.name.ilike('%a%'))
    for state in del_state:
        my_session.delete(state)
    my_session.commit()
