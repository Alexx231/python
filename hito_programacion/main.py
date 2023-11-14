from clientes import *
from articulos import *
from compras import *
from menu_app import * 

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