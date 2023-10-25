from mod_agenda import *
            
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
