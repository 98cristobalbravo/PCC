def obtener_nombre_completo(nombre: str, apellido:str, sgdo_apellido=""):
    if sgdo_apellido:
        nombre_completo = f"{nombre} {apellido} {sgdo_apellido}"
    else:
        nombre_completo = f"{nombre} {apellido}"
    return nombre_completo.title()

musico = obtener_nombre_completo("charly", "garcia", "moreno")
print(musico)