#!/usr/bin/python3
"""
module state_model
"""
from sqlalchemy import MetaData, Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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
