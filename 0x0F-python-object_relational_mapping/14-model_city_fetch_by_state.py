#!/usr/bin/python3
"""
Module 14-model_city_fetch_by_state
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    my_session = Session()

    cities = my_session.query(State.name, City.id, City.name).join(
        State).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
