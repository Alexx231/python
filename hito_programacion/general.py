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

def rellenar_lista():
    try:
        with open("clientes.txt","articulos.txt","r") as archivo:
            lista = archivo.readlines()
    except FileNotFoundError:
        print(f"\nNo ha sido posible registrar")
    return lista