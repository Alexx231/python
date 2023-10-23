#Script para leer archivos de texto

with open("mi_archivo.txt", "r") as archivo:
    contenido =  archivo.read()
    print (contenido)
    
archivo.close