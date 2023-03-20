#!/usr/bin/python3
"""
A script that lists all states with a nme starting with 'N'
(upper N) from the database 'htbn_0e_0_usa'
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

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    con.close()
