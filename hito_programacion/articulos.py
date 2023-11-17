articulos = []

# La función registrar_articulo solicita al usuario el nombre y el tipo de un artículo, 
# y luego intenta agregar esta información a un archivo llamado "articulos.txt".
def registrar_articulo():
    try:
        nombre_articulo = input(f"\nDime el nombre del articulo: ")
        tipo_articulo = input(f"\nDime el tipo de articulo que es: ")
        with open("articulos.txt","a") as archivo:
            archivo.write("\n" + nombre_articulo + "," + tipo_articulo)
            print(f"\nEl articulo {nombre_articulo} ha sido registrado correctamente")
    except FileNotFoundError:
        print(f"\nEl proceso de registro fue erroneo")
    return

# La función ver_articulos intenta abrir el archivo "articulos.txt" y muestra todos los artículos registrados.
def ver_articulos():
    try:
        with open("articulos.txt","r") as archivo:
            lineas =  archivo.readlines()
            for linea in lineas:
                nombre_articulo,tipo_articulo = linea.strip().split(",")
                print(f"\nArticulo : {nombre_articulo} - Tipo de articulo : {tipo_articulo}")
    except FileNotFoundError:
        print(f"\nNo hay articulos registrados") 
    return

# La función buscar_articulo solicita al usuario el nombre de un artículo para buscarlo en el archivo "articulos.txt".
def buscar_articulo():
    articulo_a_buscar = input(f"\nQue articulo desea buscar? : ")
    encontrado = False
    try:
        with open("articulos.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if articulo_a_buscar in linea:
                    encontrado = True
            if encontrado:
                print(f"\nEl articulo {articulo_a_buscar} esta disponible")
            else:
                print(f"\nEl articulo no esta disponible")
    except FileNotFoundError:
        print(f"\nNo se ha podido visualizar los articulos")
    return
        
# La función eliminar_articulo solicita al usuario el nombre de un artículo para eliminarlo del archivo "articulos.txt".
def eliminar_articulo():
    articulo_a_eliminar = input(f"\nQue articulo desea eliminar? :")
    articuloseliminados = []
    eliminado = False
    try:
        with open("articulos.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if articulo_a_eliminar in linea:
                    print(f"\nEl articulo {articulo_a_eliminar} fue eliminado correctamente ")
                    eliminado = True
                else:
                    articuloseliminados.append(linea)
            if eliminado:
                with open("articulos.txt","w") as archivo:
                    for linea in articuloseliminados:
                        archivo.write(linea)
    except FileNotFoundError:
        print(f"\nNo se ha podido eliminar el articulo") 
    return                    