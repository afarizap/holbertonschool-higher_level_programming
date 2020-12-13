#!/usr/bin/env python3
""" lists all states from the database hbtn_0e_0_usa, importa solo cuando se
 llama el main los argumentos y el modulo MySQL, Se asignan los valores
a buscar y se conecta la base de datos, se inicializa el cursor y se
ejecuta el query deseado, se devuelven todos los resultados dentro de la
variable r, Se itera en r cada linea para imprimir"""

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
    cursor.close()
    dbn.close()
