import mysql.connector

def conexion_empresa():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="curso",
            database=""
            )
    except mysql.connector.Error as e:
        print(f"\nLa conexion no pudo ser realizada",e) 

def cerrar_conexion(conexion_empresa):
    try:
        conexion_empresa.close()
    except mysql.connector.Error as error:
        print("La conexion no fue realizada")
        return None
