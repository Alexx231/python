compras = []

def realizar_compra():
    nombre_cliente = (f"Dime el nombre del cliente que esta realizando la compra:")
    producto_a_comprar = (f"Que producto desea comprar?:")
    unidades = (f"Cuantas unidades desea comprar?:")
    try:
        with open("articulos.txt","r") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                producto = linea.strip().split(",")
                if producto_a_comprar in producto[1]:
                    with open("compras.txt","a") as archivo:
                         archivo.write(f"{nombre_cliente} - {unidades} - {producto[1]}\n")
                         print(f"\nEl cliente{nombre_cliente} ha comprado {unidades} unidades de{producto[1]}\n")
                         seguimiento_compra()
    except ValueError:
        print(f"No se pudo realizar la compra")
    return
                
    
    
    
    
def seguimiento_compra():
    print(f"\n¡Gracias por tu compra! Tu pedido ha sido procesado.")