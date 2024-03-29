#!/usr/bin/python3
"""
module 2-filter_states
"""
import MySQLdb


def main(uname, passw, dbname, state_name):
    """
    Implements script to run an SQL querry that filters states by user input
    Args:
        uname (string): username
        passw (string): password
        dbname (string): database name
        state_name (string): name of state to search
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=uname, password=passw, database=dbname)
    cur = db.cursor()
    sql_querry = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                ORDER BY id ASC".format(state_name)
    cur.execute(sql_querry)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    from sys import argv

    uname = argv[1]
    passw = argv[2]
    dbname = argv[3]
    state_name = argv[4]

    main(uname, passw, dbname, state_name)
