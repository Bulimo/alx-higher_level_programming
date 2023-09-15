#!/usr/bin/python3
"""
Module 8-model_state_fetch_first
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
    data = my_session.query(State).order_by(State.id).first()
    if data is None:
        print("Nothing")
    else:
        print("{}: {}".format(data.id, data.name))
