#!/usr/bin/python3
"""
Module 12-model_state_update_id_2
t changes the name of a State object from the database hbtn_0e_6_usa
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
    state = my_session.get(State, 2)
    # state = my_session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    my_session.add(state)
    my_session.commit()
