respuestas = {}

votacion_activa = True

while votacion_activa:
    nombre = input("Cual es tu nombre?: ")
    respuesta = input("Que montaña blabla..: ")
    
    respuestas[nombre] = respuesta
    
    repetir = input("Quieres ingresar otro? (si/no) ")
    if repetir.lower() == "no":
        votacion_activa = False
    
print(respuestas)