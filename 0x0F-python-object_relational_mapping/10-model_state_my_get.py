#!/usr/bin/python3
"""
prints the State.id object of name passed as argument
from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


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
    stn = sys.argv[4]
    instance = session.query(State).filter(State.name == stn).first()
    if instance:
        print("{}".format(instance.id))
    else:
        print("Not found")
