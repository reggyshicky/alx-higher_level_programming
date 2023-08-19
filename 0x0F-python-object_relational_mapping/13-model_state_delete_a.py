#!/usr/bin/python3
"""
scrpitt that deletes all states objects with a name containing
the letter a from the database
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    s = session.query(State).filter(State.name.like('%a%')).all()

    for state in s:
        session.delete(state)

    session.commit()
    session.close()
