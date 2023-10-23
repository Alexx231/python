#Script que abre y escribe en un archivo de texto
archivo = open("mi_archivo.txt", "w")


archivo.write("Hola Mundo")



archivo.close




#Crea un archivo de texto y escribir dentro una lista


mi_lista = ["manzana", "platano", "cereza"]

with open("frutas.txt", "w") as archivo:
    for fruta in mi_lista:
        archivo.write(fruta + "\n")
        
archivo.close()