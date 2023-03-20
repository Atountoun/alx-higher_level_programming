#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb as sql


if __name__ == '__main__':

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # prevent sql injection
    state_name = sys.argv[4].split(';')[0]

    con = sql.connect(
            host='localhost', port=3306, user=user,
            passwd=password, db=db_name)

    cur = con.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
    cur.execute(
            query, (state_name,)
            )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    con.close()
