# Crear una lista de libros disponibles
libros_disponibles = ["Libro 1", "Libro 2", "Libro 3", "Libro 4", "Libro 5"]

# Función para mostrar los libros disponibles
def mostrar_libros_disponibles():
    print("Libros disponibles:")
    for libro in libros_disponibles:
        print(libro)

# Función para prestar un libro
def prestar_libro():
    libro = input("Ingrese el nombre del libro que desea prestar: ")
    if libro in libros_disponibles:
        libros_disponibles.remove(libro)
        print(f"Usted ha prestado '{libro}'.")
    else:
        print(f"El libro '{libro}' no está disponible en la biblioteca.")

# Función para devolver un libro
def devolver_libro():
    libro = input("Ingrese el nombre del libro que desea devolver: ")
    libros_disponibles.append(libro)
    print(f"Gracias por devolver '{libro}'.")

# Bucle principal del programa
while True:
    print("Menú de opciones:")
    print("1. Ver los libros disponibles")
    print("2. Prestar un libro")
    print("3. Devolver un libro")
    print("4. Salir del sistema")
    
    opcion = input("Seleccione una opción (1/2/3/4): ")
    
    if opcion == "1":
        mostrar_libros_disponibles()
    elif opcion == "2":
        prestar_libro()
    elif opcion == "3":
        devolver_libro()
    elif opcion == "4":
        print("¡Gracias por usar nuestro sistema de gestión de biblioteca!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4).")
