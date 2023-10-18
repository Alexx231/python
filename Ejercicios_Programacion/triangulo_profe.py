#Definicion de funcion necesaria

def calcular_area(base , altura):
    resultado = (base * altura) /2
    return resultado


#Programa Principal

base = int(input("Dime la base de tu triangulo : "))
altura = int(input("Dime la altura del triangulo : "))

area = calcular_area(base , altura) 

print(f"El area del triangulo es {area}")