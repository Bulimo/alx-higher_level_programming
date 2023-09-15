#!/usr/bin/python3
"""
module 3-filter_states
"""
import MySQLdb


def main(uname, passw, dbname, state_name):
    """
    Implements script to run an SQL querry that filters states by user input
    but checking for SQL injection
    Args:
        uname (string): username
        passw (string): password
        dbname (string): database name
        state_name (string): name of state to search
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=uname, password=passw, database=dbname)
    cur = db.cursor()
    sql_querry = "SELECT * FROM states WHERE name LIKE BINARY %s \
                ORDER BY id ASC"
    cur.execute(sql_querry, (state_name,))
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
