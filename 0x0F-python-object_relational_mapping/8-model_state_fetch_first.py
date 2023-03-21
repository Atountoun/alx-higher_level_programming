#!/usr/bin/python3
"""
This module is used to print the first `State` object from the database
`hbtn_0e_6_uda`
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
    state = session.query(State).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")
