#!/usr/bin/env python3
""" lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb

if __name__ == "__main__":
    usr = sys.argv[1]
    pss = sys.argv[2]
    dbn = sys.argv[3]

    # usr = "root"
    # pss = "0"
    # dbn = "hbtn_0e_0_usa"

    dbc = MySQLdb.connect(user=usr, passwd=pss, db=dbn)

    cursor = dbc.cursor()
    cursor.execute("SELECT * FROM states")

    r = cursor.fetchall()

    for i in r:
        print(i)
