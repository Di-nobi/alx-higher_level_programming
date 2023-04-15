#!/usr/bin/python3
"""
 a script that prints the first State object from the database hbtn_0e_6_usa
 """

 if __name__ == '__main__':
     import MySQLdb
     import SQLAlchemy
     from model_state import Base, State

     engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
     Base.metadata.create_all(engine)

     Session = sessionmaker(bind=engine)
     session = Session()
     state = session.query(State).first()
     if (!state):
         print ('Nothing')
     else:
         print("{}: {}".format(state.id, state.name))
    session.close()
