from conexion import Conectar
class Libro:
    
    def __init__(self, conectar):
        self.conectar = conectar

    def anadir(self, titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado):
        cursor = self.conectar.conexion.cursor()
        query = ("INSERT INTO libros "
                          "(titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado) "
                          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        valores = (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado)
        cursor.execute(query, valores)
        self.conectar.conexion.commit()
        cursor.close()
        print("Libro agregado correctamente.")
        
        

    def ver_libros(self):
        cursor = self.conectar.conexion.cursor()
        query = ("SELECT * FROM libros")
        cursor.execute(query)
        for(id_libro,titulo,autor,edicion,editorial) in cursor:
            print("ID:{id_libro} - Titulo:{titulo} - Autor:{autor} - Edicion:{edicion} - Editorial:{editorial}")
        self.conectar.conexion.commit()
        self.conectar.conexion.close()
        cursor.close()
        return

    def buscar_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        buscar_libro_query = ("SELECT * FROM libros WHERE titulo = %s")
        cursor.execute(buscar_libro_query, (titulo,))
        libro = cursor.fetchone()
        cursor.close()
        print(libro)
        return libro
    def eliminar_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        eliminar_libro_query = ("DELETE FROM libros WHERE titulo = %s")
        cursor.execute(eliminar_libro_query, (titulo,))
        self.db.conexion.commit()
        cursor.close()
        print("Libro eliminado corretamente.")

    def modificar_libro(self, titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado):
        cursor = self.db.conexion.cursor()
        modificar_libro_query = ("UPDATE libros SET titulo = %s, autor = %s, genero = %s, paginas = %s, anio_publicacion = %s, edicion = %s, idioma = %s, ISBN = %s, prestamos_realizados = %s, prestado = %s WHERE titulo = %s")
        libro_data = (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado, titulo)
        cursor.execute(modificar_libro_query, libro_data)
        self.db.conexion.commit()
        cursor.close()
        print("Libro modificado correctamente.")
    def prestra_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        prestar_libro_query = ("UPDATE libros SET prestado = %s WHERE titulo = %s")
        libro_data = (True, titulo)
        cursor.execute(prestar_libro_query, libro_data)
        self.db.conexion.commit()
        cursor.close()
        print("Libro prestado correctamente.")
    def devolver_libro(self, titulo):
        cursor = self.db.conexion.cursor()
        devolver_libro_query = ("UPDATE libros SET prestado = %s WHERE titulo = %s")
        libro_data = (False, titulo)
        cursor.execute(devolver_libro_query, libro_data)
        self.db.conexion.commit()
        cursor.close()
        print("Libro devuelto correctamente.")