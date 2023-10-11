calificaciones = []


def añadir_calificaciones(calificaciones):
    #Esta fncion añadira un elemento a la lista de notas
    nota = input("\nPorfavor Introduzca una nueva nota")
    calificaciones.append(int(nota))
    return calificaciones


def media_calificaciones(calificaciones):
    #Esta funcion calculara y devolvera la nota media de la lista de notas
    media = sum(calificaciones)/len(calificaciones)
    print(f"La media de notas es: {media}")
    return


def calificacion_mas_alta(calificaciones):
    #Esta funcion devolvera la nota mas alta
    print(f"La calificacion mas alta es: {max(calificaciones)}")
    return


def calificacion_mas_baja(ca):
    #Esta funcion devolvera la nota mas baja
    print(f"La calificacion mas baja es: {min(calificaciones)}")
    return

def ver_notas(calificaciones):
    #Esta funcion nos mostrara el contenido de la lista de notas
    for nota in calificaciones:
        print(f"{nota}")
    return


def menu():
    #Esta funcion visualizara el menu y devolvera la opcion elegida
    print("\nMENU DE OPCIONES\n")
    print("\n1.- Añadir notas")
    print("\n2.- Ver notas")
    print("\n3.- Ver media de notas")
    print("\n4.- Ver mayor nota")
    print("\n5.- Ver menor notas")
    print("\n6.- Salir")
    opcion=int(input("\nSeleccione una opcion de las opciones dadas : "))
    
    return int(opcion)




#operativa principal del script
#un bucle nfinito hasta que la opcion del usuario sea salir

while True:
    #visualizar el menu
    opcion = menu()
    #En funcion de la opcion elegida
        #Añadir elemento a la lista
        #Ver notas
        #Ver nota media
        #Ver nota mas alta
        #Ver nota mas baja
        #Salir
    if opcion == 1:
            calificaciones = añadir_calificaciones(calificaciones)
    elif opcion == 2:
            ver_notas(calificaciones)
    elif opcion == 3:
            media_calificaciones(calificaciones)
    elif opcion == 4:
            calificacion_mas_alta(calificaciones)
    elif opcion == 5:
            calificacion_mas_baja(calificaciones)
    elif opcion == 6:
            print("\n\n HASTA PRONTO")
            break
    else:
        print(f"Sigue Intentandolo")
            
        
        

         