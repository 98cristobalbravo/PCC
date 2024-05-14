num_favoritos = {
    "pam": 1,
    "jim": 4,
    "michael": 6,
    "kevin": 0,
    "creed": 9
}

for nombre in num_favoritos:
    valor = num_favoritos[nombre]
    print(nombre, valor)

if "pepito" not in num_favoritos.keys():
    print("Por favor, pepito escoge un numero.")
else:
    print("Gracias a todos")    
    
    
num_favoritos["juan"] = 2
num_favoritos["juana"] = 2
num_favoritos["pedro"] = 55
num_favoritos["cat"] = 3
