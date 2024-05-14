for numero in range(1, 6):
    print(numero)
    
for numero in range(6):
    print(numero)
    
numeros = range(6)
print(numeros)

lista = list(numeros)
print(lista)

numeros = list(range(0, 6))
print(numeros)

tabla_cinco = list(range(0, 55, 5))
print(tabla_cinco)

numeros_cuadrados = []
for numero in range(1, 11):
    cuadrado = numero ** 2
    numeros_cuadrados.append(cuadrado)
print(numeros_cuadrados)

cuadrado_breve = []
for numero in range(1, 11):
    cuadrado_breve.append(numero**2)
print(cuadrado_breve)

digitos = list(range(10))
print(digitos)
print(min(digitos))
print(max(digitos))
print(sum(digitos))

cuadrados = [valor**2 for valor in range(1, 11)]
print(cuadrados)

tablaCinco = [c*5 for c in range(11)]
print(tablaCinco)