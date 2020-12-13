#!/usr/bin/env python3
""" lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    """ importa solo cuando se llama el main los argumentos y el modulo MySQL"""
    import sys
    import MySQLdb

    """ Se asignan los valores a buscar y se conecta la base de datos"""
    usr = sys.argv[1]
    pss = sys.argv[2]
    dbn = sys.argv[3]

    dbc = MySQLdb.connect(user=usr, passwd=pss, db=dbn)

    """ se inicializa el cursor y se ejecuta el query deseado """
    cursor = dbc.cursor()
    cursor.execute("SELECT * FROM states")

    """ se devuelven todos los resultados dentro de la variable r """
    r = cursor.fetchall()

    """ Se itera en r cada linea para imprimir"""
    for i in r:
        print(i)
