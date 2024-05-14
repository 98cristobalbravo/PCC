nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Laura", "Diego", "Sofía", "Luis", "Elena"]

longitud = len(nombres)
medio = longitud//2

if longitud % 2 == 0:
    inicio = medio - 1
else:
    inicio = medio - 1
    
print(nombres[inicio:inicio+3])
    
    
    
for primero in nombres[:3]:
    print(primero)