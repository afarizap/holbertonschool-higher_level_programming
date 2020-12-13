#!/usr/bin/python3
""" takes in an argument and displays all values in
 the states table of hbtn_0e_0_usa where name matches the argument """
import sys
import MySQLdb


if __name__ == "__main__":
    usr = sys.argv[1]
    pss = sys.argv[2]
    dbn = sys.argv[3]
    stn = sys.argv[4]

    dbc = MySQLdb.connect(user=usr, passwd=pss, db=dbn)

    cursor = dbc.cursor()
    cursor.execute("SELECT * FROM states WHERE name={!r}".format(stn))

    r = cursor.fetchall()

    for i in r:
        print(i)
