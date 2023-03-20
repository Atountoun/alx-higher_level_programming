#!/usr/bin/python3
"""
Module that contains the class definition of a 'State' based on
the declarative way of 'SQLAlchemy'
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    State object to be mapped with states table in the database:
    """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
