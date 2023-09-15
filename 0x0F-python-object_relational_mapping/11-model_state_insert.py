#!/usr/bin/python3
"""
Module 11-model_state_insert
adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    new_state = State(name="Louisiana")
    my_session.add(new_state)
    my_session.commit()
    print(new_state.id)
