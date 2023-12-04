""" Realizar préstamos y devoluciones de libros """

def realizarprestamo(prestamo_a_realizar):
    try:
        conexionbdd = Conectar()
        cursor = conexionbdd.cursor()
        query = "UPDATE libros SET prestamos_realizados = %s WHERE id_libro = %s"
        valores = prestamo_a_realizar
        cursor.execute(query,valores)
        conexionbdd.commit()
        print("El préstamo fue realizado correctamente")
        conexionbdd.close()
    except mysql.connector.Error as error:
        print("El préstamo fue cancelado",error)
        
def realizardevolucion(devolucion_a_realizar):
    try:
        conexionbdd = Conectar()
        cursor = conexionbdd.cursor()
        query = "UPDATE libros SET prestamos_realizados = %s WHERE id_libro = %s"
        valores = devolucion_a_realizar
        cursor.execute(query,valores)
        conexionbdd.commit()
        print("La devolución fue realizada correctamente")
        conexionbdd.close()
    except mysql.connector.Error as error:
        print("La devolución fue cancelada",error)