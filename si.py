calistenia = ["dominadas","flexiones","fondos","barras","sexo","alcohol","drogas","porros","fumar","morir"]
contador = 0
while True:
    guess=str(input("Dime un elemento: " ))
    if guess == "salir":
        print("Gracias por usar este programa ")
        break
    

    elif guess in calistenia:
        calistenia.append(0)
        print(calistenia)
        print("Has acertado, majo: ")
      
    elif guess not in calistenia:
        calistenia.pop(-1)
        print(calistenia)

        