#!/usr/bin/python3
"""
    Create a City in a State in certain Database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    new_state = State(name='California')
    new_city = City(name='San Francisco')
    new_state.citites = [new_city]

    session.add(new_state)
    session.add(new_city)
    session.commit()

    session.close()
    engine.dispose()
