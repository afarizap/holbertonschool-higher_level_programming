#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    """ take 3 arguments: mysql username, mysql password and database name """
    usr = sys.argv[1]
    pss = sys.argv[2]
    dbn = sys.argv[3]
    """ from MySQLdb module """
    dbc = MySQLdb.connect(user=usr, passwd=pss, db=dbn)

    with dbc.cursor() as cursor:
        cursor.execute(
            "SELECT cities.id, cities.name, states.name\
            FROM cities INNER JOIN states ON cities.state_id = states.id")
        r = cursor.fetchall()

    for i in r:
        print(i)
