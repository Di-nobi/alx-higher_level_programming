#!/usr/bin/python3
"""A python file that contains the class definition of a city"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
