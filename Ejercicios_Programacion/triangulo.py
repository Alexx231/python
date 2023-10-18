def calculararea(base, altura)
resultado = 


def menu():
    print("1. Calcular el area del triangulo")
    print("2. No quiero calcular el area del triangulo")
    opcion = input("Elige de forma numerica : ")
    return (int(opcion))

while True:
    opcion = menu()
    if opcion == 1:
        area_triangulo()
    elif opcion == 2:
        print("Adios")
        break