#!/usr/bin/python3
"""
module relationship_state
contains the class definition of a State with relationship to City and an
instance Base = declarative_base()
"""
from sqlalchemy import MetaData, Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    states class implementation

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state')
