#!/usr/bin/python3
"""Shows all City objects from database"""

from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ =="__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for ins_state, ins_city in session.query(State.name, City.id, City.name).filter(State.id == City.state_id):
        print("{} : ({}) {}".format(ins_state.name, ins_city.id, ins_city.name))
