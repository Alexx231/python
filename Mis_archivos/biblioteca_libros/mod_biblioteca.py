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

def menu(): #Menu de Programa
    print(f"\n1. Añadir un libro")
    print(f"\n2. Ver libros")
    print(f"\n3. Buscar un libro")
    print(f"\n4. Eliminar un libro")
    print(f"\n5. Prestar un libro")
    print(f"\n6. Devolver un libro")
    print(f"\n7. Ver libro prestado")
    opcion = int(input(f"\nSelecciona una opcion : "))
    return opcion

def añadirlibro(): #Funcion que permitira al usuario añadir a la lista (biblioteca) un libro con su titulo,autor,año de publicacion y genero 
    try:
        titulo = input(f"\nDime el titulo del libro : ")
        autor = input(f"\nDame el autor del libro : ")
        year = input(f"\nEn que año se publico el libro? : ")
        genero = input(f"\nDime el genero del libro : ")
        with open("biblioteca.txt","a") as archivo:
            archivo.write(titulo + "," + autor + "," + year + "," + genero + "\n")
            print(f"\nEl libro {titulo} fue añadido correctamente")
    except FileNotFoundError:
        print(f"\nNo se pudo añadir el libro")
    return

def visualizarlibros(): #Funcion que nos muestra una lista con todos los libros agregados
    try:
        with open("biblioteca.txt","r") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                titulo,autor,year,genero = linea.strip().split(",")
                print(f"\nTitulo : {titulo} - Autor : {autor} - Año de Publicacion : {year} - Genero : {genero}")
    except FileNotFoundError:
        print(f"\nNo hay libros disponnibles") 
    return

def buscarlibros(): #Funcion que permite buscar un libro en concreto de dentro de la lista(biblioteca) y imprimirlo en pantalla
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

def eliminarlibros(): #Funcion que permite eliminar un libro de la lista 
    libro_a_eliminar = input(f"\nQue libro desea eliminar? : ")
    libroseliminados = []
    eliminado = False
    
    try:
        with open("biblioteca.txt", "r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                titulo,autor,year,genero = linea.strip().split(",")
                if titulo == libro_a_eliminar:
                    textoaguardar = titulo + "," + autor + "," + year + "," + genero + "\n"
                    libroseliminados.append(textoaguardar)
                else:
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

    
                
def prestarlibro(): #Funcion que registra un libro en concreto que ha sido prestado
    libro_a_prestar = input(f"\nDime el libro que quieras prestar : ")
    librosprestados = []
    prestado = False
    try:
        with open("biblioteca.txt","r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    titulo,autor,year,genero = linea.strip().split(",")
                    if libro_a_prestar in linea:
                        textoaguardar = titulo + "," + autor + "," + year + "," + genero + "\n"
                        librosprestados.append(textoaguardar)
                        prestado = True
                if prestado:
                    with open("biblioteca.txt", "w") as archivo:
                        for linea in librosprestados:
                            archivo.write(linea)
                    print(f"\nEl libro {libro_a_prestar} ha sido prestado ")
                    
                    with open("bibliotecaprestados.txt", "a") as prestado:
                        prestado.write(f"\nEl libro que ha sido prestado es {libro_a_prestar}")
                    
    except FileNotFoundError:
        print(f"\nNo a sido posible prestar el libro")
    return

            

def devolverlibro(): #Funcion que devuelve a la lista(biblioteca) un libro prestado 
    libros_devolver = input(f"\nDime un libro que quieras devolver : ")
    librosdevueltos = []
    devuelto = False
    try:
        with open("bibliotecaprestados.txt","r") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                if libros_devolver in linea:
                    print(f"\nEl libro {libros_devolver} ha sido devuelto")
                    librosdevueltos.append(linea)
                    devuelto = True
            if devuelto:
                with open("bibliotecaprestados.txt", "w") as archivo:
                    for libro in librosdevueltos:
                        archivo.write(f"\nlibro")
                with open("biblioteca.txt", "a") as archivo:
                    archivo.write(f"\n{libro}")
    except FileNotFoundError:
        print(f"\nNo se pudo devolver el libro")
    return
    
    
def visualizarlibrosprestados(): #Funcion que permite visualizar los libros que hay dentro de la lista de libros prestados
    with open("bibliotecaprestados.txt","r") as archivo:
        lineas =  archivo.readlines()
        for linea in lineas:
            titulo,autor,year,genero = linea.strip().split(",")
            print(f"\nTitulo : {titulo} - Autor : {autor} - Año de Publicacion : {year} - Genero : {genero}")  
    return

