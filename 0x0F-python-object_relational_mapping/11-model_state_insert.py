#!/usr/bin/python3
"""
scripts that adds the State object "Louisiana"
to the database
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    s = session.query(State).filter_by(name="Louisiana").first()
    # first() is used to retrieve the first occurence that matches
    # your query criteria
    if s:
        print(s.id)

    session.close()
