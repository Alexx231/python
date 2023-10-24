diario = []


def menu():
    print(f"\n1.Añadir al diario")
    print(f"\n2.Ver el diario")
    print(f"\n3.Eliminar del diario")
    print(f"\n4.Salir")
    opcion = input(f"\nElige una opcion : ")
    return opcion


def anadir_diario():
    


def ver_diario():
    

def eliminar_diario():


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