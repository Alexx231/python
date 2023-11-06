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
    
    print("\nComenzamos la insercion de un nuevo registro")
     
    cursor = conexion.cursor()
    query = "INSERT INTO producto (nombre,idproducto) VALUES (%s,%s)"
    valores = ["Fardastopa Radioactiva",200]
    cursor.execute(query, valores)
    conexion.commit()
    print("Usuario añadido con éxito.")
    cursor.close()
    conexion.close()

    
except mysql.connector.Error as e:
    print("Error al conectar a la base de datos: ", e)
    
   
    
    
