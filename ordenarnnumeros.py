#Crear un programa que pida al usuario ingresar varios números y los ordene de menor a mayor sin utilizar métodos de ordenación predefinidos.
#Implementar funciones y bucles para realizar la ordenación y mostrar los números ordenados al usuario.


numeros_ordenados = []

def numerosordenados(numeros_ordenados):
    for numeros in numeros_ordenados:
        print(f"{numeros}", end_=" ")


while True:
    opcion = str(input(f"\nDime los numeros : "))
    numeros_ordenados = numerosordenados(numeros_ordenados)
    if opcion == "Salir":
        print(f"\nGracias, vuelva pronto")
        break
    else:
        print(f"Intentalo de nuevo")
     