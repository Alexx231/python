clientes = []

# La función registro_cliente solicita al usuario el nombre, apellido, teléfono y DNI de un cliente, 
# y luego intenta agregar esta información a un archivo llamado "clientes.txt".
def registro_cliente():
    try:
        nombre = input(f"\nDime el nombre del cliente: ")
        apellido = input(f"\nDime el apellido del cliente: ")
        telefono = input(f"\nDime el telefono del cliente: ")
        dni = input(f"\nDime el numero de identificacion del cliente: ")
        with open("clientes.txt","a") as archivo:
            archivo.write("\n" + nombre + "," + apellido + "," + telefono + "," + dni)
            print(f"\nEl cliente {nombre} fue registrado correctamente")
    except FileNotFoundError:
        print(f"\nEl proceso de registro fue erroneo")
    return

# La función ver_cliente intenta abrir el archivo "clientes.txt" y muestra todos los clientes registrados.
def ver_cliente():
    try:
        with open("clientes.txt","r") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                nombre,apellido,telefono,dni = linea.strip().split(",")
                print(f"\nNombre y Apellido : {nombre} {apellido} - Telefono : {telefono} - DNI: {dni}")
    except FileNotFoundError:
        print(f"\nNo hay clientes registrados")
    return

# La función buscar_clientes solicita al usuario el nombre de un cliente para buscarlo en el archivo "clientes.txt".
def buscar_clientes():
    cliente_a_buscar = input(f"\nQue cliente desea buscar: ")
    encontrado = False
    try:
        with open("clientes.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if cliente_a_buscar in linea:
                    encontrado = True
            if encontrado:
                print(f"\nEl cliente {cliente_a_buscar} esta registrado")
            else:
                print(f"\nEl cliente no esta registrado")
    except FileNotFoundError:
        print(f"\nError")
    return

# La función eliminar_clientes solicita al usuario el nombre de un cliente para eliminarlo del archivo "clientes.txt".
def eliminar_clientes():
    cliente_a_eliminar = input(f"\nQue cliente desea eliminar? :")
    clienteseliminados = []
    eliminado = False
    try:
        with open("clientes.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if cliente_a_eliminar in linea:
                    print(f"\nEl cliente {cliente_a_eliminar} fue eliminado correctamente ")
                    eliminado = True
                else:
                    clienteseliminados.append(linea)
            if eliminado:
                with open("clientes.txt","w") as archivo:
                    for linea in clienteseliminados:
                        archivo.write(linea)
    except FileNotFoundError:
        print(f"\nNo se ha podido eliminar el cliente") 
    return                    