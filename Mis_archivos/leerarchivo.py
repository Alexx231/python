#Script para leer archivos de texto
lista = []


with open("mi_archivo.txt","r") as archivo:
    contenido =  archivo.read()
    print(contenido)
      
archivo.close()

#Leer listas desde un archivo de texto

with open("frutas.txt","r") as archivo:
    frutas = archivo.readline()
    
    
    for fruta in frutas:
        lista.append(fruta)
    
    
    print(frutas)
    
    
    print("\nEsta es la lista llamada lista", lista)
    