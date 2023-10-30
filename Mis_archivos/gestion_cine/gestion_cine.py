from mod_cine import *    
    
while True:
    opcion = menu()
    
    if opcion == 1:
        cine = anadirpelicula()
    elif opcion == 2:
        visualizarpeliculas()
    elif opcion == 3:
        buscarpelicula()
    elif opcion == 4:
        cine = eliminarpelicula()
    elif opcion == 5:
        print(f"\nHASTA LA PROXIMA")
        break
    else:
        print(f"\nLa opcion seleccionada no existe")