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
Biblioteca = []

def menu():
    print(f"\n1. Añadir un libro")
    print(f"\n2. Ver libros")
    print(f"\n3. Buscar un libro")
    print(f"\n4. Eliminar un libro")
    print(f"\n5. Prestar un libro")
    print(f"\n6. Devolver un libro")
    print(f"\n7. Ver libro prestado")
    opcion = int(input(f"\nSelecciona una opcion : "))
    return opcion

def añadirlibro():
    try:
        Titulo = input(f"\nDime el titulo del libro : ")
        Autor = input(f"\nDame el autor del libro : ")
        Año_de_publicacion = input(f"\nEn que año se publico el libro? : ")
        Genero = input(f"\nDime el genero del libro : ")
        with open("biblioteca.txt","a") as archivo:
            archivo.write(Titulo + "," + Autor + "," + Año_de_publicacion + "," + Genero + "\n")
            print(f"\nEl libro {Titulo} fue añadido correctamente")
    except FileNotFoundError:
        print(f"\nNo se pudo añadir el libro")
    return

def visualizarlibros():
    try:
        with open("biblioteca.txt","r") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                Titulo,Autor,Año_de_publicacion,Genero = linea.strip().split(",")
                print(f"\nTitulo : {Titulo} - Autor : {Autor} - Año de Publicacion : {Año_de_publicacion} - Genero : {Genero}")
    except FileNotFoundError:
        print(f"\nNo hay libros disponnibles") 
    return

def buscarlibros():
    libro_a_buscar = input(f"\nQue libro deseas buscar :")
    encontrado = False
    try:
        with open("biblioteca.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if libro_a_buscar in linea:
                    encontrado = True
            if encontrado:
                print(f"\nEl libro {libro_a_buscar} esta disponible ")
            else:
                print(f"\nEl libro no esta disponible")
    except FileNotFoundError:
        print(f"\nEl libro que intentas buscar, no esta disponible")
    return

def eliminarlibros():
    libro_a_eliminar = input(f"\nQue libro desea eliminar? : ")
    libroseliminados = []
    eliminado = False
    
    try:
        with open("biblioteca.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                Titulo,Autor,Año_de_publicacion,Genero = linea.strip().split(",")
                if Titulo in libro_a_eliminar:
                    libroseliminados.append(linea)
                    eliminado = True
            if eliminado:
                with open("biblioteca.txt", "w") as archivo:
                    for linea in libroseliminados:
                        archivo.write(linea)
                print(f"\nEl libro {libro_a_eliminar} fue eliminado correctamente")
            else:
                print(f"\nEl libro no se encontró en la biblioteca")
    except FileNotFoundError:
        print(f"\nEl libro no pudo ser eliminado")
    return

    
                
def prestarlibro():
    libro_a_prestar = input(f"\nDime el libro que quieras prestar : ")
    librosprestados = []
    prestado = False
    try:
        with open("bibliotecaprestados.txt","r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    Titulo,Autor,Año_de_publicacion,Genero = linea.strip().split(",")
                    if libro_a_prestar in linea:
                        librosprestados.append(linea)
                        prestado = True
                if prestado:
                    with open("bibliotecaprestados.txt", "w") as archivo:
                        for linea in librosprestados:
                            archivo.write(linea)
                    print(f"\nEl libro {libro_a_prestar} fue prestado exitosamente")
                else:
                    print(f"\nEl libro no se encontró en la biblioteca")
    except FileNotFoundError:
        print(f"\nNo a sido posible prestar el libro")
    return

            

def devolverlibro(Biblioteca):
    libros_devolver = input(f"\nDime un libro que quieras devolver : ")
    try:
        with open("bibliotecaprestados.txt","a") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                if linea in Biblioteca:
                    Biblioteca.append(linea)
    except FileNotFoundError:
        print(f"\nNo se pudo devolver el libro")
    return Biblioteca
    
    
def visualizarlibrosprestados():
    with open("bibliotecaprestados.txt","r") as archivo:
        lineas =  archivo.readlines()
        for linea in lineas:
            Titulo,Autor,Año_de_publicacion,Genero = linea.strip().split(",")
            print(f"\nTitulo : {Titulo} - Autor : {Autor} - Año de Publicacion : {Año_de_publicacion} - Genero : {Genero}")  
    return

