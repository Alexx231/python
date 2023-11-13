from clientes import *
from articulos import *
from compras import *

def menu():
    print(f"\nBIENVENIDO AL PROGRAMA")
    print(f"1. Registro de Cliente")
    print(f"2. Ver Clientes")
    print(f"3. Buscar Cliente")
    print(f"4. Eliminar Cliente")
    print(f"5. Realizar Compra")
    print(f"6. Seguimiento de Compra")
    print(f"7. Registro de Articulo")
    print(f"8. Ver Articulos")
    print(f"9. Buscar Articulo")
    print(f"10. Eliminar Articulo")
    print(f"11. Salir")
    opcion = input(f"\nQue desea hacer?")
    return (int(opcion))



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