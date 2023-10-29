from mod_biblioteca import *

while True:
    opcion = menu()
    
    if opcion == 1:
        Biblioteca = añadirlibro()
    elif opcion == 2:
        visualizarlibros()
    elif opcion == 3:
        buscarlibros()
    elif opcion == 4:
        Biblioteca = eliminarlibros()
    elif opcion == 5:
        Biblioteca = prestarlibro()
    elif opcion == 6:
        Biblioteca = devolverlibro(Biblioteca)
    elif opcion == 7:
        visualizarlibrosprestados()
        break
    else:
        print(f"\nLa opcion seleccionada no es valida ")
    