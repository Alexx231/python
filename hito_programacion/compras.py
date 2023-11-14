from clientes import *
from articulos import *

compras = []

def seguimiento_compra():
    print(f"\n¡Gracias por tu compra! Tu pedido ha sido procesado.")
    
def realizar_compra():
    ver_articulos()
    nombre_cliente = input(f"Dime el nombre del cliente que esta realizando la compra:")
    producto_a_comprar = input(f"Que producto desea comprar?:")
    unidades = input(f"Cuantas unidades desea comprar?:")
    productoscomprados = []
    try:
        with open("articulos.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                producto = linea.strip().split(",")
                if producto_a_comprar in producto[1]:
                    productoscomprados.append(producto)
                with open("compras.txt","a") as archivo:
                        archivo.write(f"\nEl cliente {nombre_cliente} ha comprado {unidades} unidades de {producto[1]}")
                seguimiento_compra()
                break
    except FileNotFoundError:
        print(f"No se pudo realizar la compra")
    return