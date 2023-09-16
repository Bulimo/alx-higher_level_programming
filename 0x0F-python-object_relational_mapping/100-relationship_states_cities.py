#!/usr/bin/python3
"""
module 100-relationship_states_cities
creates tables states and cities in the database
populates the database with an object of State and City
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # run the create_all() twice to create both tables
    Base.metadata.create_all(engine)
    Base.metadata.create_all(engine)

    # create an instance of the State and populate the cities attr
    calif = State(name="California")
    calif.cities = [City(name="San Francisco")]

    # create a session add and commit the new state
    Session = sessionmaker(bind=engine)
    my_session = Session()

    my_session.add(calif)
    my_session.commit()
    my_session.close()
