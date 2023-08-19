#!/usr/bin/python3
"""
script that lists all State objecs from the db
"""

if __name__ == "__main__":
    import sys  # allow interaction with cmdline args
    from model_state import Base, State
    from sqlalchemy import create_engine  # used to create a connection to db
    from sqlalchemy.orm import Session  # manages sessions with the db

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    # pool_pre_ping=True enables a feature that checks the db liveness
    # before using it from the pool
    Base.metadata.create_all(engine)
    """
    creates the necessary tables in the db based on the definitio of
    in the Base class(sqlalchemy declaritive base)
    Declarative_base is a function in sqlalchemy used to create a base
    class for declaritive models.sqlalchemy's declarative extension
    allows you to define your data models as python classes, which are
    then used to automatically generate the corresponding db tables and
    provide an object-oriented way to interact with the db
    """
    session = Session(engine)
    # session created to interact with db using the previously created engine
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        # queries all state objects and sort by id

    session.close()
