persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "Ciudad": "Santiago"
}

num_favoritos = {
    "pam": 1,
    "jim": 4,
    "michael": 6,
    "kevin": 0,
    "creed": 9
}

print(f"El numero favorito de pam es: {num_favoritos["pam"]}")
print(f"El numero favorito de jim es: {num_favoritos["jim"]}")
print(f"El numero favorito de michael es: {num_favoritos["michael"]}")
print(f"El numero favorito de kevin es: {num_favoritos.get("kevi2n")}")
print(f"{num_favoritos.get("creeed", "No encontrado")}")

num_favoritos["kelly"] = 1
print(num_favoritos)
print(f"Kelly num fav: {num_favoritos.get("kelly")}")

for nombre, valor in num_favoritos.items():
    print(f"Nombre: {nombre.title()} - N° favorito: {valor}")
    
#for nombre, valor in sorted(num_favoritos.keys(), num_favoritos.values()):
#    print(nombre, valor)


    
for valor in set(num_favoritos.values()):
    print(valor)