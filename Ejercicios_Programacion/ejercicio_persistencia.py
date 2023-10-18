from io import open
archivo_texto = open("archivo.txt", "w")# w significa que es un archivo de tipo texto
frase = "Este archivo de texto creado es de Alejandro Pawlukiewicz"
archivo_texto.write(frase)
archivo_texto.close() 

#a raiz de la creacion del archivo_texto lo demas son formas de interactuar con el
#el from io import open siempre es para iniciar la ruta en la cual se inicia el codigo
# archivo.txt que es lo que esta en el parentesis de la segunda linea es el nombre del archivo que se va a ver, antes del = es el valor del cual va a salir ese nombre