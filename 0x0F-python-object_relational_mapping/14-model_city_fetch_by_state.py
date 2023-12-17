#!/usr/bin/python3
"""a script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    database = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])

    engine = create_engine(database)
    Session = sessionmaker(bind=engine)
    session = Session()

    output = session.query(City, State).join(State)

    for city, state in output.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()
