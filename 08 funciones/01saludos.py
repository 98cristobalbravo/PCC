def saludar():
    print("Hola")
saludar()
    
def saludar_usuario(usuario: str):
    print(f"Hola, {usuario.title()}")

saludar_usuario('juanita')

def libro_favorito(libro: str):
    print(f"Mi libro favorito es, {libro.title()}")
    
libro_favorito("Alicia en el país de las maravillas.")