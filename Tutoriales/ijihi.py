mascotas = ["perro","gato","caballo","alex"]
contador = 0
while True: 
    usuario = str(input("Elige una mascota :"))
    if usuario == "salir":
        print("Gracias, vuelva pronto")
        break
    if usuario in mascotas :
        print("Acertaste")
        contador = contador + 1
        print(contador)
    else:
        mascotas.pop(usuario)
        print("Sigue intentandolo")
       