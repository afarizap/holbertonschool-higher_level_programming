#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """
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
    instance = session.query(State).order_by(State.id)[0]
    if instance:
        print("{}: {}".format(instance.id, instance.name))
    else:
        print("Nothing")
