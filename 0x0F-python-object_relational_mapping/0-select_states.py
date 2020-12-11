#!/usr/bin/env python3
""" lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    import sys
    import MySQLdb

    usr = sys.argv[1]
    pss = sys.argv[2]
    dbn = sys.argv[3]

    dbc = MySQLdb.connect(user=usr, passwd=pss, db=dbn)

    cursor = dbc.cursor()
    cursor.execute("SELECT * FROM states")

    r = cursor.fetchall()

    for i in r:
        print(i)
