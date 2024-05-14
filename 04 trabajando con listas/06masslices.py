numeros = [1, 2, 3, 4, 5, 6, 7]
longitud = len(numeros)
print(longitud)
medio = longitud // 2
print(medio)

if longitud % 2 == 0:
    inicio = medio - 1
    cantidad = 2
    print(numeros[inicio:inicio+cantidad])
else:
    inicio = medio - 1
    cantidad = 3
    print(numeros[inicio:inicio+cantidad])

