"""
Desarrollar un programa que permita gestionar las películas y las funciones en un cine con el paradigma de la Programación Orientada a Objetos:
    
Agregar una película: Cada película debe tener un título, director, duración (en minutos) y clasificación (ej. PG, PG-13, PG-18, PG+18).

Visualizar todas las películas: Mostrar una lista de todas las películas disponibles en el cine.

Buscar una película por título o director: Permitir al usuario buscar una película específica.

Eliminar una película: Permitir al usuario eliminar una película de la lista.
"""

class peliculas:
    
    def __init__(self, titulo, director, duracion, clasificacion):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        self.clasificacion = clasificacion
        
        
    def añadirpelicula(self):
        try:
            print(f"Añadir película: {self.titulo}")
            print("Ingrese los datos de la película")
            print(f"Director: {self.director}")
            print(f"Duracion: {self.duracion}")
            print(f"Clasificacion: {self.clasificacion}")
            with open("peliculas.txt", "a") as archivo:
                archivo.write(f"{self.titulo},{self.director},{self.duracion},{self.clasificacion}\n")
        except FileNotFoundError:
            print("No se ha encontrado la pelicula")
        return
        
    def verpeliculas(self):
        try:
            with open("peliculas.txt", "r") as archivo:
                for linea in archivo:
                    print(linea)
        except FileNotFoundError:
            print("No se ha encontrado la pelicula")
        return
    
    def buscarpelicula(self):
        pelicula_a_buscar = input(f"\nDime la pelicula que quieres buscar : ")
        try:
            with open("peliculas.txt", "r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    if pelicula_a_buscar in linea:
                        print(f"\nLa pelicula {pelicula_a_buscar} esta en el catalogo")
                        return
        except FileNotFoundError:
            print(f"\nLa pelicula {pelicula_a_buscar} no esta disponible")
            return
    
    
    def eliminarpelicula(self):
        pelicula_a_eliminar = input(f"\nDime la pelicula que deseas eliminar : ")
        peliculaseliminadas = []
        eliminado = False
        try:
            with open("peliculas.txt","r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    if pelicula_a_eliminar in linea:
                        print(f"\nLa pelicula {pelicula_a_eliminar} ha sido eliminada correctamente ")
                        eliminado = True
                    else:
                        peliculaseliminadas.append(linea)
                if eliminado:
                    with open("peliculas.txt","w") as archivo:
                        for linea in peliculaseliminadas:
                            archivo.write(linea)
        except FileNotFoundError:
            print(f"\nNo se a podido eliminar la pelicula") 
        return


mis_peliculas = peliculas("Donkey Kong","Gabriel","2 Horas","PG-12")

mis_peliculas.añadirpelicula("Mario Bros","Juan","1 Hora y 30 Minutos","PG-16")

            


    

        
        
        
