#!/usr/bin/python3
"""
script that prints the State object with the name passed as arg
from the db
"""
if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    neme = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    s = session.query(State).filter(State.name == neme).first()
    if s:
        print("{}".format(s.id))
    else:
        print("Not found")
    session.close()
