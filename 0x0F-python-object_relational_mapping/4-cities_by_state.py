#!/usr/bin/python3
"""
Script that lists all 'cities' from the database 'hbtn_0e_4_usa'
"""
import sys
import MySQLdb as sql


if __name__ == '__main__':

    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    con = sql.connect(
            host='localhost', port=3306, user=user,
            passwd=password, db=db_name)

    cur = con.cursor()
    query = """
    SELECT c.id, c.name, s.name FROM cities AS c
    JOIN states AS s
    ON c.state_id = s.id
    ORDER BY c.id
    """
    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    con.close()
