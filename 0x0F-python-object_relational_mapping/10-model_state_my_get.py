#!/usr/bin/python3
"""
This module is used to print the `State` object with the `name`
passed as argument from the database `hbtn_0e_6_uda`
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4].split(';')[0]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        user,
        password,
        db),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    state_ids = session.query(State.id).filter(State.name == state_name).all()

    if len(state_ids):
        for state_id in state_ids:
            print(state_id[0])
    else:
        print("Not found")
