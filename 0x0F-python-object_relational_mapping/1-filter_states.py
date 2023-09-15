#!/usr/bin/python3
"""
module 1-filter_states
"""
import MySQLdb


def main(uname, passw, dbname):
    """
    Implements script to run an SQL querry that filters states
    Args:
        uname (string): username
        passw (string): password
        dbname (string): database name
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=uname, password=passw, database=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
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
