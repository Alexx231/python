""" añadir y borrar """


from conexion import Conectar

def anadirlibro(libros_a_guardar):
    try:
        conexionbdd = Conectar()
        cursor = conexionbdd.cursor()
        query ="INSERT INTO libros (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        valores = libros_a_guardar
        cursor.execute(query,valores)
        conexionbdd.commit()
        print("El proceso de añadir el libro fue hecho correctamente")
        conexionbdd.close()
    except mysql.connector.Error as error:
        print("El proceso de añadir al cliente fue cancelado",error)

anadirlibro()
