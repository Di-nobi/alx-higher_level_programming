#!/usr/bin/python3
""" Creates a State with a City"""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)
    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
