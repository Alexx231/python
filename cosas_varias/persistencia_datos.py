import mysql.connector

conexion = mysql.connector.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_contraseña',
    database='nombre_de_tu_base_de_datos'
)
cursor = conexion.cursor()
query = "INSERT INTO usuarios (nombre, email, fecha_registro) VALUES (%s, %s, %s)"
valores = ("Juan Pérez", "juanperez@example.com", "2023-01-01")
cursor.execute(query, valores)
conexion.commit()
print("Usuario añadido con éxito.")
cursor.close()
conexion.close()
