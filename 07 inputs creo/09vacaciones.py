respuestas = dict()
encuesta_activa = True

while encuesta_activa:
    nombre = input("Nombre: ")
    destino = input("Destino: ")
    
    respuestas[nombre] = destino
    
    encuesta_activa = input("Añadir mas personas? (si/no) -> ")
    
    if encuesta_activa == "no":
        encuesta_activa = False

for nom, dest in respuestas.items():
    nom = f"Nombre: {nom.title()}"
    dest =f"\tDestino: {dest.title()}\n"
    print(nom)
    print(dest)