"""

Desarrollar un programa que permita gestionar los libros de una biblioteca.
 
Agregar un libro: Cada libro debe tener un título, autor, año de publicación y género.

Visualizar todos los libros: Mostrar una lista de todos los libros en la biblioteca.

Buscar un libro por título o autor: Permitir al usuario buscar un libro específico.

Eliminar un libro: Permitir al usuario eliminar un libro de la biblioteca.

Prestar un libro: Registrar cuándo un libro ha sido prestado y a quién.

Devolver un libro: Registrar cuándo un libro ha sido devuelto.

Visualizar libros prestados: Mostrar una lista de todos los libros que están prestados y quién los tiene.

"""

def agregarlibro():
    try:
        Titulo = input(f"\nDime el titulo del libro : ")
        Autor = input(f"\nDame el autor del libro : ")
        Año_de_publicacion = input(f"\nEn que año se publico el libro? : ")
        Genero = input(f"\nDime el genero del libro : ")
        with open("biblioteca.txt","w") as archivo:
            archivo.write(Titulo + ";" + Autor + ";" + Año_de_publicacion + ";" + Genero + "\n")
            print(f"\nEl libro {Titulo} fue añadido correctamente")
    except FileNotFoundError:
        print(f"\nNo se pudo añadir el libro")
    return