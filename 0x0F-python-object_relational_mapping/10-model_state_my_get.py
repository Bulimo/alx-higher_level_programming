#!/usr/bin/python3
"""
Module 10-model_state_my_get
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import NoResultFound

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    my_session = Session()
    try:
        data = my_session.query(State).filter(
            State.name == sys.argv[4]).one()
        print("{}".format(data.id))
    except NoResultFound:
        print("Not found")
