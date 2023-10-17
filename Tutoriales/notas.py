notas = []

def menu():
    print("Opciones : ")
    print("Añadir nuevas notas : ")
    print("3 Nota más alta")
    print("4 Nota más baja")
    print("5 Salir")
    
    def nuevas_notas(notas):
        nota = (input("Dime la nota : "))
        notas.append(nota)
        return notas
    
    
    def nota_media(notas):
        media = sum(notas)/len(notas)
        print("La nota media es", media)
        return notas
    
    
    def notamásalta(notas): 
        nota_maxima = max(notas)
        print("La nota más alta es", nota_maxima)
        return notas
    
    
    def notamásbaja(notas): 
        nota_minima = min(notas)
        print("La nota más baja es", nota_minima)
        return notas
    
    
    while True:
        opcion = menu()
        if opcion == 1:
            notas = nuevas_notas(notas)
        elif opcion == 2:
            notas = nota_media(notas)
        elif opcion == 3:
            notas = notamásalta(notas)
        elif opcion == 4:
            notas = notamásbaja(notas)
        elif opcion == 5:
            print("Gracias,vuelva pronto")
            
        break
    
    