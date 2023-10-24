diario = [] #Lista vacia en la que se introduciran valores 


def menu(): #Funcion que muestra un menú con opciones para añadir al diario, ver el diario, eliminar del diario o salir.
    print(f"\n1.Añadir al diario")
    print(f"\n2.Ver el diario")
    print(f"\n3.Eliminar del diario")
    print(f"\n4.Salir")
    opcion = int(input(f"\nElige una opcion : "))
    return opcion


def anadir_diario(diario): #Funcion que permite al usuario agregar un día y una anécdota. Los valores se introducen manualmente y se escriben en el archivo "diario.txt"
    try:
        dia = input(f"Introducir un dia : ") #Para pedirle al usuario que introduzca un dia manualmente
        anecdota = input(f"Introcudir una anectota : ") #Para pedirle al usuario que introduzca una anecdota manualmente
        with open("diario.txt", "a") as archivo: #Se utiliza para abrir el archivo de texto donde se almacenan los valores introducidos por el usuario 
                                                    #Y el "a" significa append que sirve para añadir valores en este caso al archivo de texto
            archivo.write(dia + ";" + anecdota + "\n") 
            print(f"\nSe a añadido correctamente el dia {dia}")
    except FileNotFoundError:
        print(f"\nOpcion Incorrecta")
    return diario
       
def ver_diario(diario): #Funcion que lee el archivo "diario.txt" y muestra el contenido, que son los días y las anécdotas previamente ingresadas.
    try:
        with open("diario.txt","r")as archivo: #Se utiliza para abrir el archivo de texto donde se almacenan los valores introducidos por el usuario 
                                                    #Y el "r" significa read que sirve para leer valores en este caso del archivo de texto
            lineas = archivo.readlines() #Para que lea linea por linea
            for linea in lineas:
                dia,anecdota = linea.strip().split(";") #Para que quite los espacios que hay y los ; ( punto y coma)
                print(f"Dia {dia} - Anecdota {anecdota}")
    except FileNotFoundError:
        print(f"Parece ser que el dia no es correcto, intentalo de nuevo")
    return diario
           
def eliminar_diario(diario): #Funcion que permite al usuario eliminar un día específico del diario.
    dia_a_eliminar = input("Introduce el nombre del contacto que deseas eliminar : ")
    fechas = []
    eliminado = False
    try:
        with open("diario.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                dia,anecdota = linea.strip().split(";")
                if dia != dia_a_eliminar:
                    fechas.append({dia,anecdota})
                else:
                    eliminado = True
                    
            if eliminado:
                with open("diario.txt","w") as archivo:
                    for dia in fechas:
                        archivo.write(dia[0]+ ";" + dia[1])
    except FileNotFoundError:
        print(f"\nPorfavor, intentelo de nuevo")
        
    return diario
                
                
                
                
                
while True: #Funcion Principal
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
