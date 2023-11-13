
def rellenar_lista():
    try:
        with open("clientes.txt","articulos.txt","r") as archivo:
            lista = archivo.readlines()
    except FileNotFoundError:
        print(f"\nNo ha sido posible registrar")
    return lista