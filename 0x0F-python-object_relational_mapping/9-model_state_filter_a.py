#!/usr/bin/python3
"""
Module 9-model_state_filter_a
lists all State objects that contain the letter a
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
    data = my_session.query(State).order_by(
        State.id).filter(State.name.like('%a%'))
    for elem in data:
        print("{}: {}".format(elem.id, elem.name))
