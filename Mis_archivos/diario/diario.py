diario = []


def menu():
    print(f"\n1.Añadir al diario")
    print(f"\n2.Ver el diario")
    print(f"\n3.Eliminar del diario")
    print(f"\n4.Salir")
    opcion = int(input(f"\nElige una opcion : "))
    return opcion


def anadir_diario(diario):
    dia = input(f"Introducir un dia : ")
    anecdota = input(f"Introcudir una anectota : ")
    with open("diario.txt", "a") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            linea.strip().split(";")
        print(dia + ";" + anecdota)
    return diario
            
        
def ver_diario():
    

def eliminar_diario():
    return


while True:
    opcion = menu()
    
    if opcion == 1:
        anadir_diario()
    elif opcion == 2:
        ver_diario()
    elif opcion == 3:
        eliminar_diario()
    elif opcion == 4:
        print(f"\nHASTA LA PROXIMA")
        break
    else:
        print(f"\nIntentalo de nuevo")