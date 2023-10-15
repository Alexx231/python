#Crear un programa que permita al usuario añadir vehículos a un registro, visualizar el registro, y eliminar vehículos de él. 
#Cada vehículo debe tener una marca, modelo y año de fabricación. 
#Utiliza funciones para añadir, visualizar y eliminar vehículos, y utiliza bucles y condicionales para gestionar las opciones del usuario.

registro_de_coches = ["Volkswagen Golf 2015","Fiat 500L 2010","Peugeot 5008 2020"]

def visualizar_registro(registro_de_coches):
    #Esta funcion permite visualizar la lista
    for vehiculo in registro_de_coches:
     print(f"{vehiculo}")
    return



def anadirvehiculos(registro_de_coches):
    #Esta funcion permitira añadir vehiculos a la lista de coches
    vehiculo = str(input(f"\nPorfavor añade un vehiculo : "))
    registro_de_coches.append(vehiculo)
    return registro_de_coches



def devolvervehiculo(registro_de_coches):
    #Esta funcion permite remover el vehiculo de la lista
    vehiculo = str(input(f"\nPorfavor escoge el vehiculo que desea devolver : "))
    registro_de_coches.remove(vehiculo)
    return registro_de_coches


def menu():
    print("\nMENU DE OPCIONES : ")
    print("\n1. Visualizar registro : ")
    print("\n2. Añadir vehiculo : ")
    print("\n3. Devolver vehiculo : ")
    print("\n4. Salir : ")
    opcion = int(input(f"\nSeleccione una de las opciones dadas : "))
    return opcion

#Funcion Principal
while True:
    opcion = menu()
    
    if opcion == 1:
        visualizar_registro(registro_de_coches)
    elif opcion == 2:
        registro_de_coches = anadirvehiculos(registro_de_coches)
    elif opcion == 3:
        registro_de_coches = devolvervehiculo(registro_de_coches)
    elif opcion == 4:
        print(f"\n\n HASTA PRONTO")
        break
    else:
        print(f"Sigue Intentandolo")

    
    