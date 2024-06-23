#!/usr/bin/python3

"""
    Pyt Cde Use ORM
"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()


class State(Base):
    """
        State Class inherent from Base
        (attrbiutes):
            id : unique
            name: max of 128
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

