def obtener_nombre_completo(primer_nombre:str, apellido:str):
    nombre_completo = f"{primer_nombre} {apellido}"
    return nombre_completo.title()


obtener_nombre_completo("nombre", "apellido")

pintor = obtener_nombre_completo(primer_nombre="jackson", apellido="Pollock")
print(pintor)