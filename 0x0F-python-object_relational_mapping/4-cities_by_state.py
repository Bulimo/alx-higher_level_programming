#!/usr/bin/python3
"""
module 4-cities_by_states
"""
import MySQLdb


def main(uname, passw, dbname):
    """
    Implements script to run an SQL querry that lists cities by states
    Args:
        uname (string): username
        passw (string): password
        dbname (string): database name
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=uname, password=passw, database=dbname)
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    import sys

    uname = sys.argv[1]
    passw = sys.argv[2]
    dbname = sys.argv[3]

    main(uname, passw, dbname)
