#!/usr/bin/python3
"""
module 4-cities_by_states
"""
import MySQLdb


def main(uname, passw, dbname, state_name):
    """
    Implements script to run an SQL querry that filters cities by states
    Args:
        uname (string): username
        passw (string): password
        dbname (string): database name
        state_name (string): name of state to search
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=uname, password=passw, database=dbname)
    cur = db.cursor()
    sql_query = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name = BINARY %s ORDER BY cities.id ASC"
    cur.execute(sql_query, (state_name,))
    rows = cur.fetchall()
    if len(rows) == 0:
        print()
    else:
        tup = ()
        for row in rows:
            tup += row
        for i in range(len(tup)):
            if i == len(tup) - 1:
                print(tup[i])
            else:
                print(tup[i], end=', ')

    cur.close()
    db.close()


if __name__ == "__main__":
    from sys import argv

    uname = argv[1]
    passw = argv[2]
    dbname = argv[3]
    state_name = argv[4]

    main(uname, passw, dbname, state_name)
