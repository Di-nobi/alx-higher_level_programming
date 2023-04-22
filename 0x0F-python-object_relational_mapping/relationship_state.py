#!/usr/bin/python3
"""
Stores an instance od declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
storemetadata = MetaData()
Base = declarative_base(metadata=storemetadata)

class State(Base):
    """
    id and name attributes of each state
    """
    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
