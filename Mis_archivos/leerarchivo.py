#Script para leer archivos de texto



with open('mi_archivo.txt','r') as archivo:
    contenido =  archivo.read()
    print(contenido)
      
archivo.close()

#Leer listas desde un archivo de texto
lista = []
with open("frutas.txt","r") as archivo:
    frutas = archivo.readline()
    
    #Utilizamos el metodo .strip para eliminar todos los espacios iniciales y finales, 
    #Asi como los tabuladores o saltos de linea del string
    for fruta in frutas:
        lista.append(fruta.strip())
    
    
    print(frutas)
    
    
    print("\nEsta es la lista llamada lista", lista)
    