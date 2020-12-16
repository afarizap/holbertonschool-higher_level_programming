#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    """ create all the data based on .sql file engine == Source ,
    metadata.create_all() is like exec"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    """ we start talking to de db, with the orm module we define Session class
    which will serve as a factory for new session objects"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """ querying """
    ob = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in ob:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
