#!/usr/bin/python3
""" add a relationship with cities """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    """ state class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, index=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
