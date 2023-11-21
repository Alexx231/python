from clientes import *
from articulos import *

compras = []

# La función seguimiento_compra imprime un mensaje de agradecimiento por la compra.
def seguimiento_compra():
    print(f"\n¡Gracias por tu compra! Tu pedido ha sido procesado. En breves momentos, le enviaremos un SMS para que pueda ir haciendo el seguimiento de su pedido.")
    return

# La función realizar_compra muestra todos los artículos disponibles, solicita al usuario el nombre del cliente que realiza la compra, 
# El producto que desea comprar y la cantidad de unidades. Luego, intenta abrir el archivo "articulos.txt" para verificar la disponibilidad del producto.
# Si el producto está disponible, se registra la compra en el archivo "compras.txt" y se llama a la función seguimiento_compra.
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
                if producto_a_comprar in producto:
                    productoscomprados.append(producto)
                    with open("compras.txt","a") as archivo:
                        archivo.write(f"\nEl cliente {nombre_cliente} ha comprado {unidades} unidades de {producto[0]}")
                    seguimiento_compra()
                    break
    except FileNotFoundError:
        print(f"No se pudo realizar la compra")
    return