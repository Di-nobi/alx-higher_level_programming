#!/usr/bin/python3
"""
a script that prints the State object with the name passed as
argument from the database
"""

if __name__ == '__main__':
    from model_state import State, Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    try:
        print("{}".format(state.id))
    except NameError:
        print("Not found")
