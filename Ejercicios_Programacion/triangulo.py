def area_triangulo():
    base = int(input("Dime la base :"))
    altura = int(input("Dime la altura : "))
    area = (base * altura) /2
    print(f"El area es {area}")


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