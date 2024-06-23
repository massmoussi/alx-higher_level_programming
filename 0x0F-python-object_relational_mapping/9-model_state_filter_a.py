#!/usr/bin/python3

"""
    xxx
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import asc


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    result = session.query(State.id, State.name)\
        .filter(State.name.like('%a%')).order_by(asc(State.id)).all()

    for id, name in result:
        print("{}: {}".format(id, name))

    session.close()
    engine.dispose()
