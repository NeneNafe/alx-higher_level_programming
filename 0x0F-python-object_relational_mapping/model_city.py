#!/usr/bin/python3
"""a file  that contains the class definition of a State and
an instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """State class that represents the cities table in MySQL."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
