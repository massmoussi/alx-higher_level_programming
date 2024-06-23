#!/usr/bin/python3

"""
    fetch all stt content
    Usng ORM query
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    results = session.execute(select(State).filter_by(id=2)).scalar_one()
    results.name = 'New Mexico'
    session.commit()

    session.close()
    engine.dispose()
