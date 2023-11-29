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
        self.devuelto = False
        self.edicion = edicion
        self.prestamos_realizados = prestamos_realizados
        self.isbn = ISBN
        self.id_libro = id_libro
    
    
    def visualizarlibros(self):
        print(f"Los libros a mostrar son los siguientes: ")
        print(f"Nombre: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Genero: {self.genero}")
        print(f"Editorial: {self.editorial}")
        
    def buscarlibros(self, titulo, autor):
        if self.titulo == titulo or self.autor == autor:
            return True
        return False
    
    def eliminarlibros(self, titulo, id_libro):
        if self.titulo == titulo or self.id_libro == id_libro:
            return True
        return False
    
    def prestarlibros(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolverlibros(self):
        if not self.devuelto:
            self.devuelto = True
            return True
        return False
            
    
    
