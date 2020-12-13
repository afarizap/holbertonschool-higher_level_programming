#!/usr/bin/python3
"""  takes in the name of a state as an argument and
 lists all cities of that state, using the database hbtn_0e_4_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    """ take 4 arguments: mysql username, mysql password, database name
    and state name (SQL injection free!) """
    usr = sys.argv[1]
    pss = sys.argv[2]
    dbn = sys.argv[3]
    stn = sys.argv[4]
    """ from MySQLdb module connect code with database"""
    dbc = MySQLdb.connect(user=usr, passwd=pss, db=dbn)
    """ with cursor function execute query """
    with dbc.cursor() as cursor:
        cursor.execute(
            "SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", (stn, ))
        r = cursor.fetchall()
    """ print each row of results """
    out = ""
    for i in r:
        out += i[0] + ", "
    print(out[:-2])
