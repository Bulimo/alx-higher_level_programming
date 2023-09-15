#!/usr/bin/python3
"""
module state_city
Implements the class definition of city
"""
from sqlalchemy import MetaData, Column, Table, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    cities class implementation

    Args:
        Base (_type_): _description_
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
