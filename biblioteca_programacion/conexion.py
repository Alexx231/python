import mysql.connector

class Conectar:
    
    def conexion_biblioteca(self):
        try:
            conexionbdd= mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            print(f"La conexion fue exitosa")
        except mysql.connector.Error as e:
            print(f"\nLa conexion no pudo ser realizada",e)
            