#!/usr/bin/python3

"""
    Python Code Use ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """
        City Class inherent from Base
        (attrbiutes):
            id : unique
            name: max of 128
            state_id: Foreign key of states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
