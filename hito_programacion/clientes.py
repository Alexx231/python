"""
print(f"\n1. Registro de Cliente")
print(f"\n2. Ver Clientes")
print(f"\n3. Buscar Cliente")
print(f"\n4. Eliminar Cliente")
"""

def registro_cliente():
    try:
        Nombre = (f"\nDime el nombre del cliente: ")
        Apellido = (f"\nDime el apellido del cliente: ")
        Telefono = (f"\nDime el telefono del cliente: ")
        DNI = (f"\nDime el numero de identificacion del cliente: ")
        with open("clientes.txt","a") as archivo:
            archivo.write(Nombre + "," + Apellido + "," + Telefono + "," + DNI + "\n")
            print(f"\nEl cliente {Nombre} fue registrado correctamente")
    except FileNotFoundError:
        print(f"\nEl proceso de registro fue erroneo")
    return

def ver_cliente():
    try:
        with open("clientes.txt","r") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                Nombre,Apellido,Telefono,DNI = linea.strip().split(",")
                print(f"\nNombre y Apellido : {Nombre} {Apellido} - Telefono : {Telefono} - DNI {DNI}")
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
    
    
        
        
    