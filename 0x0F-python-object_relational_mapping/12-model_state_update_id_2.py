#!/usr/bin/python3
"""
This module is used to change the name of a `State` object
with id = 2 to `New Mexico` from the database `hbtn_0e_6_uda`
"""
import sys
from model_state import Base, State

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

    state = session.query(State).get(2)
    state.name = 'New Mexico'

    session.commit()
