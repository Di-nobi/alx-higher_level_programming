#!/usr/bin/python3
"""
a script that adds the State object “Louisiana” to the database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    rec_state = session.query(State).filter(State.name =='Louisiana').first()
    print(rec_state.id)
    session.commit()
    session.close()
