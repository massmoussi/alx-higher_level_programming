#!/usr/bin/python3

"""
    stt fetch
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(bind=engine)

    result = session.query(State.id, State.name).first()
    if result:
        id, name = result
        print("{}: {}".format(id, name))
    else:
        print("Nothing")

    session.close()
    engine.dispose()
