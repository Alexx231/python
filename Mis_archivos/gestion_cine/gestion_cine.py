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
    
def visualizarpeliculas():
    
def buscarpelicula():
    
def eliminarpelicula():
    
    
while True:
    opcion = menu()
    
    if opcion == 1:
        anadirpelicula()
    elif opcion == 2:
        visualizarpeliculas()
    elif opcion == 3:
        buscarpelicula()
    elif opcion == 4:
        eliminarpelicula()
    elif opcion == 5:
        print(f"\nHASTA LA PROXIMA")
        break
    else:
        print(f"\nLa opcion seleccionada no existe")