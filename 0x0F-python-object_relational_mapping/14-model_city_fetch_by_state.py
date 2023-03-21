#!/usr/bin/python3
"""
This module is used to print all `State` objects
from the database `hbtn_0e_14_uda`
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user,
        password,
        db),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).\
            order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
