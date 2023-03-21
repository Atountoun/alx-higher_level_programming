#!/usr/bin/python3
"""
This module is used to define a mapping class `City` to the
database table cities
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """
    Mapping object to the database table
    """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
