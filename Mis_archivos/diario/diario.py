diario = []


def menu():
    print(f"\n1.Añadir al diario")
    print(f"\n2.Ver el diario")
    print(f"\n3.Eliminar del diario")
    print(f"\n4.Salir")
    opcion = int(input(f"\nElige una opcion : "))
    return opcion


def anadir_diario(diario):
    try:
        dia = input(f"Introducir un dia : ")
        anecdota = input(f"Introcudir una anectota : ")
        with open("diario.txt", "a") as archivo:
            diario.append(dia + ";" + anecdota)
            print(f"\nSe a añadido correctamente el dia {dia}")
    except FileNotFoundError:
        print(f"\nOpcion Incorrecta")
    return diario

          
def ver_diario(diario):
    try:
        with open("diario.txt","r")as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                dia,anecdota = linea.strip().split(";")
                print(f"Dia {dia} - Anecdota {anecdota}")
    except FileNotFoundError:
        print(f"Parece ser que el dia no es correcto, intentalo de nuevo")
    return diario
           
def eliminar_diario(diario):
    dia_a_eliminar = input(f"\nEscribe el dia que desees eliminar : ")
    dias= []
    eliminado = False
    
    
    try:
        with open("diario.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                dia,anecdota = linea.strip().split(";")
                if dia in dia_a_eliminar:
                    diario.append(dia,anecdota)
                else:
                    eliminado = True
            if eliminado:
                 with open("diario.txt","w") as archivo:
                    for dia in dias:
                        archivo.write(dia[0] + ";" + dia[1])
    except FileNotFoundError:
        print(f"\nPorfavor, intentelo de nuevo")
                             
    return diario
                
                
        
            
    


while True:
    opcion = menu()
    
    if opcion == 1:
        diario = anadir_diario(diario)
    elif opcion == 2:
        ver_diario(diario)
    elif opcion == 3:
        diario = eliminar_diario(diario)
    elif opcion == 4:
        print(f"\nHASTA LA PROXIMA")
        break
    else:
        print(f"\nIntentalo de nuevo")
