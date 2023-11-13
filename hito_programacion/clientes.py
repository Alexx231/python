"""
print(f"\n1. Registro de Cliente")
print(f"\n2. Ver Clientes")
print(f"\n3. Buscar Cliente")
print(f"\n4. Eliminar Cliente")
"""

def registro_cliente():
    try:
        nombre = (f"\nDime el nombre del cliente: ")
        apellido = (f"\nDime el apellido del cliente: ")
        telefono = (f"\nDime el telefono del cliente: ")
        dni = (f"\nDime el numero de identificacion del cliente: ")
        with open("clientes.txt","a") as archivo:
            archivo.write(nombre + "," + apellido + "," + telefono + "," + dni + "\n")
            print(f"\nEl cliente {nombre} fue registrado correctamente")
    except FileNotFoundError:
        print(f"\nEl proceso de registro fue erroneo")
    return

def ver_cliente():
    try:
        with open("clientes.txt","r") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                nombre,apellido,telefono,dni = linea.strip().split(",")
                print(f"\nNombre y Apellido : {nombre} {apellido} - Telefono : {telefono} - DNI {dni}")
    except FileNotFoundError:
        print(f"\nNo hay clientes registrados") 
    return

def buscar_clientes():
    cliente_a_buscar = (f"\nQue cliente desea buscar? : ")
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

def eliminar_clientes():
    cliente_a_eliminar = (f"\nQue cliente desea eliminar? :")
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
    
        
        
    