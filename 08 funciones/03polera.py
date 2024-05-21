"""
def crear_polera(tamano: int, texto: str):
    print(f"Polera talla {tamano}, con el texto: '{texto}'")
    
crear_polera(40, "aaaaaaaaaaaaa")
crear_polera(tamano=36, texto="Hola, chao")

"""
def crear_polera(tamano: int, texto:str = "python xd"):
    print(f"Polera talla {tamano}, con el texto: '{texto}'")

crear_polera(tamano=40)

def ciudad_pais(ciudad: str, pais:str):
    print(f"{ciudad}, {pais}")
    
ciudad_pais(ciudad="puerto montt", pais="Chile")