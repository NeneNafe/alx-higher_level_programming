#!/usr/bin/python3
"""a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    """Gets the state fro mthe database"""
    engine = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if (state.name == argv[4]):
            print(state.id)
            break
    else:
        print("Not Found")
