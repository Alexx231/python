"""

Desarrollar un programa que permita gestionar las películas y las funciones en un cine.

Agregar una película: Cada película debe tener un título, director, duración (en minutos) y clasificación (ej. PG, PG-13, PG-18, PG+18).

Visualizar todas las películas: Mostrar una lista de todas las películas disponibles en el cine.

Buscar una película por título o director: Permitir al usuario buscar una película específica.

Eliminar una película: Permitir al usuario eliminar una película de la lista.

"""

def menu():
    print(f"\n1. Añadir una pelicula")
    print(f"\n2. Visualizar peliculas")
    print(f"\n3. Buscar pelicula")
    print(f"\n4. Eliminar una pelicula")
    print(f"\n5. Salir")
    
def anadirpelicula():
    titulo = input(f"\nEscribe el titulo de una pelicula : ")
    director = input(f"\nQuien es el director? : ")
    duracion = input(f"\nCuanto dura? : ")
    clasificacion = input(f"\nEscribe cual es su clasificacion : ")
    try:
        with open("cine.txt","a") as archivo:
            archivo.write(titulo + "," + director + "," + duracion + "," + clasificacion + "\n")
            print(f"\nLa pelicula {titulo} fue añadida correctamente ")
    except FileNotFoundError:
        print(f"\nNo ha sido posible añadir la pelicula ")
    return
            
            
def visualizarpeliculas():
    try:
        with open("cine.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                print(f"\n{linea}")
    except FileNotFoundError:
        print(f"\nNo hay peliculas disponibles")
            
    
def buscarpelicula():
    
def eliminarpelicula():