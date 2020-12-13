#!/usr/bin/python3
""" contains class def of state and instance base = declaratie base"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

""" Returns a new base class from which all mapped classes should inherit. """
Base = declarative_base()


class State(Base):
    """ table name """
    __tablename__ = 'states'
    """ class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key """
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, index=True)
    """ class attribute name that represents a column of a string
    with maximum 128 characters and can’t be null """
    name = Column(String(128), nullable=False)
