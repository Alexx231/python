import mysql.connector


def conexion_clientes():
    try:
        return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "curso",
        database = "empresa"
        )
    except mysql.connector.Error as Error:
        print("La conexion no pudo ser realizada")
        return None

def cerrar_conexion(conexion_clientes):
    try:
        conexion_clientes.close()
    except mysql.connector.Error as error:
        print("La conexion no fue realizada")
        return None


        



