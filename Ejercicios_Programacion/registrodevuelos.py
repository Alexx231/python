#Crear un programa que permita al usuario reservar asientos en un vuelo.
#El programa debe mostrar los asientos disponibles, permitir al usuario seleccionar un asiento, y luego actualizar la lista de asientos disponibles.
#Utiliza listas para gestionar los asientos y funciones para realizar las operaciones de reserva y visualización.

registro_vuelo = ["3A","5F","6E","9B","13C"]


def verasientos(registro_vuelo):
    #Esta funcion se utiliza para poder visualizar los asientos disponibles en el registro
    print(f"Estos son los asientos disponibles : ")
    for asientos in registro_vuelo:
        print(f"{asientos}")
        

def reservarasientos(registro_vuelo):
    #Dicha funcion sirve para poder reservar un asiento disponible y que al volver a ver la lista el asiento no aparezca ya que esta reservado
    asientos = str(input(f"Dime un asiento : "))
    if asientos in registro_vuelo:
        print(f"\nLa reserva ha sido completada")
        registro_vuelo.remove(asientos)
        return registro_vuelo
    else:
        print(f"\nEl asiento no esta disponible, porfavor escoja otro asiento")
        
        
def menu():
    print(f"\nOPCIONES : ")
    print(f"\n1. Ver asientos : ")
    print(f"\n2. Reservar asiento : ")
    print(f"\n3. Salir : ")
    opcion = int(input(f"\nSelecciona la opcion : "))
    return opcion 

#Funcion Principal
while True:
    opcion = menu()
    
    if opcion == 1:
        verasientos(registro_vuelo)
    elif opcion == 2:
        registro_vuelo = reservarasientos(registro_vuelo)
    elif opcion == 3:
        print(f"\nGRACIAS, VUELVA PRONTO")
        break
    else:
        print(f"\n Opcion Incorrecta")
        
    
    
    
        
    
        

        
