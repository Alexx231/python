#Crear un programa que permita al usuario añadir productos a una lista de compras, visualizar la lista, y eliminar productos de ella utilizando funciones, bucles y condicionales.




lista_de_compras = []


def anadirproductos(lista_de_compras):
    #Esta funcion nos permitira añadir productos a la lista de compras
    producto = input(f"\nPorfavor añade un producto : ")
    lista_de_compras.append(str(producto))
    return lista_de_compras


def visualizarlista(lista_de_compras):
    #Esta funcion nos permitira visualizar la lista de la compra
    for producto in lista_de_compras:
     print(f"{producto}")
     return
    
    
def devolverproducto(lista_de_compras):
    #Esta funcion nos permitira devolver el productoo a la lista de la compra
    producto =  input(f"\nQue producto desea devolver : ")
    lista_de_compras.remove(str(producto))
    return lista_de_compras

def menu():
    print("\nMENU DE OPCIONES : ")
    print("\n1. Visualizar lista : ")
    print("\n2. Añadir Producto : ")
    print("\n3. Devolver Producto : ")
    print("\n4. Salir : ")
    opcion = int(input(f"\nSeleccione una de las opciones dadas : "))
    return opcion
    
while True:
    
    opcion = menu()
    
    if opcion == 1:
        visualizarlista(lista_de_compras) 
    elif opcion == 2:
        lista_de_compras = anadirproductos(lista_de_compras)  
    elif opcion == 3:
        lista_de_compras = devolverproducto(lista_de_compras)
    elif opcion == 4:
        print("\n HASTA LA PROXIMA")
        
        break
    else:
        print(f"\nSigue Intentandolo")
        
    
    