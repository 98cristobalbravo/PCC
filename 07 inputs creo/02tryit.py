while True:
    edad = input("Ingresa edad: ")
    if edad == "salir":
        break
    else:        
        try:
            edad = int(edad)
            if edad < 3:
                print("Ingreso liberado")
            elif edad >= 3 and edad < 12:
                print("valor: $10")
            else:
                print("valor: $15")
        except:
            print("Por favor, ingresa un numero valido")
