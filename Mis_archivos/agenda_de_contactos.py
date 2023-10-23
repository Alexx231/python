contactos = []

def menu():
    print("\n1. Añadir Contacto")
    print("\n2. Visualizar Contacto")
    print("\n3. Eliminar Contacto")
    print("\n4. Salir")
    opcion = int(input(f"\nElige una opcion : "))
    return opcion


def anadircontactos(contactos):
    nombre = input("\nPorfavor añade un nombre : ")
    telefono = input("\nPorfavor añade un numero de telefono : ")
    with open("agenda.txt", "a") as archivo:
        archivo.write(nombre + ',' + telefono)
        print(f"Contacto {nombre} añadido correctamente")
    return contactos


def visualizar_contactos(contactos):
    try:
        with open("agenda.txt") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                nombre,telefono = linea.strip().split(',')
                print(f"Nombre {nombre} - Telefono {telefono}")
    except FileNotFoundError:
        print(f"La agenda de contacto parece estar vacia")
    return contactos
        
        

def eliminar_contacto(contactos):
    nombre_a_eliminar = input("Introduce el nombre del contacto que deseas eliminar : ")
    contactos = []
    eliminado = False
    
    try:
        with open("agenda.txt") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                nombre,telefono = linea.strip().split(',')
                if nombre in nombre_a_eliminar:
                    contactos.append({nombre, telefono})
                else:
                    eliminado = True
                    
            if eliminado:
                with open("agenda.txt") as archivo:
                    for contacto in contactos:
                        archivo.write(contacto[0]+ ','+ contacto[1])
    except FileNotFoundError:
        print(f"\nPorfavor, intentelo de nuevo")
                             
    return contactos



while True:
    opcion = menu()

    if opcion == 1:
        contactos = anadircontactos(contactos)
    elif opcion == 2:
        visualizar_contactos(contactos)
    elif opcion == 3:
        contactos = eliminar_contacto(contactos)
    elif opcion == 4:
        print(f"\nHASTA LUEGO")
        break
    else:
        print(f"\nOpcion Incorrecta")
    
    