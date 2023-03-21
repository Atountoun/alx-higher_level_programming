#!/usr/bin/python3
"""
This module is used to list all `State` objects that contain the
letter `a` from the database `hbtn_0e_6_uda`
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
    query = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for state in query:
        print('{}: {}'.format(state.id, state.name))
