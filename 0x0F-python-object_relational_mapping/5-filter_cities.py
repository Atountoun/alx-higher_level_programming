#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database 'hbtn_0e_4_usa'
"""
import sys
import MySQLdb as sql


if __name__ == '__main__':

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4].split(';')[0]

    con = sql.connect(
            host='localhost', port=3306, user=user,
            passwd=password, db=db_name)

    cur = con.cursor()
    query = """
    SELECT c.name FROM cities AS c
        JOIN states AS s
        ON c.state_id = s.id
        WHERE s.name = %s
        ORDER BY c.id
    """
    cur.execute(query, (state_name, ))
    rows = cur.fetchall()

    for row in rows:
        print(row[0], end=', ')
    print()

    cur.close()
    con.close()
