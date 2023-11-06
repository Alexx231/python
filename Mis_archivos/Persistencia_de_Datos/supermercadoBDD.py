import mysql.connector


try:
    # Establecer la conexión
    conexion = mysql.connector.connect(
        host='localhost',
        user='root',
        password='curso',
        database='supermercado'
    )
    print("Conexión exitosa.")
except mysql.connector.Error as e:
    print("Error al conectar a la base de datos: ", e)
