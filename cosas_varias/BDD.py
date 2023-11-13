import mysql.connector

def conexion_bdd():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="curso",
            database="empresa",
            )
    except mysql.connector.Error as e:
        print(f"\nLa conexion no pudo ser realizada",e) 

def cierra_conexion(conexion_bdd):
        conexion_bdd.close()
    