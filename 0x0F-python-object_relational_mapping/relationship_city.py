#!/usr/bin/python3
"""
Defines the City class.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """
    City class that inherits from Base and links to the MySQL table cities.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
