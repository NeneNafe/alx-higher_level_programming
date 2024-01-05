#!/usr/bin/python3
"""a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    del_states = session.query(State).filter(State.name.contains('a'))
    if del_states is not None:
        for state in del_states:
            session.delete(state)
    session.commit()

    session.close()