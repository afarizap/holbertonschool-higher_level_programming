#!/usr/bin/python3
""" lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa """
import sys
import MySQLdb


if __name__ == "__main__":

    usr = sys.argv[1]
    pss = sys.argv[2]
    dbn = sys.argv[3]

    dbc = MySQLdb.connect(user=usr, passwd=pss, db=dbn)

    cursor = dbc.cursor()
    cursor.execute("SELECT * FROM states")

    r = cursor.fetchall()

    for i in r:
        if i[1][0] == 'N':
            print(i)
