class libro:

    def __init__(self, titulo, autor, editorial, genero,anio_publicacion, paginas, idioma, edicion, prestamos_realizados, ISBN, id_libro):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.ano_publicacion = anio_publicacion
        self.paginas = paginas
        self.idioma = idioma
        self.prestado = False
        self.edicion = edicion
        self.prestamos_realizados = prestamos_realizados
        self.isbn = ISBN
        self.id_libro = id_libro
    
    
    def cargar_tabla_libros(self,conexion):
        cursor = conexion.cursor()
        query = ("SELECT * FROM libros")
        valores =  self.titulo, self.autor, self.editorial, self.genero, self.ano_publicacion, self.paginas, self.idioma, self.edicion, self.prestamos_realizados, self.isbn, self.id_libro, self.prestado
        cursor.execute(query,valores)
        conexion.commit()
        cursor.close()
        print("Libro cargado correctamente.")