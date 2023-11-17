from clientes import *
from articulos import *
from compras import *

# La función menu imprime un menú de opciones para el usuario y solicita una opción. 
# Devuelve la opción seleccionada como un entero.
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
    opcion = input(f"\nQue desea hacer:")
    return (int(opcion))

# Este bucle infinito mantiene el programa en ejecución hasta que el usuario decida salir.
# Llama a la función menu para obtener la opción del usuario y luego ejecuta la función correspondiente a esa opción.
while True:
    
    opcion = menu()
    
    if opcion == 1:
        clientes = registro_cliente()
    elif opcion == 2:
        ver_cliente()
    elif opcion == 3:
        buscar_clientes()
    elif opcion == 4:
        clientes = eliminar_clientes()
    elif opcion == 5:
        compras = realizar_compra()
    elif opcion == 6:
        compras = seguimiento_compra()
    elif opcion == 7:
        articulos = registrar_articulo()
    elif opcion == 8:
        ver_articulos()
    elif opcion == 9:
        buscar_articulo()
    elif opcion == 10:
        articulos = eliminar_articulo()
    elif opcion == 11:
        print(f"\nGracias por utilizar nuestro programa")
    else:
        print(f"\nLa opcion seleccionada no es valida ")