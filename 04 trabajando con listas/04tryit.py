"""
for num in range(1, 21):
    print(num)
    
nums = list(range(1, 1000001))
for num in nums:
    print(num)
    
"""

numeros = list(range(1, 1000001))
print(min(numeros))
print(max(numeros))
print(sum(numeros))

pares = list(range(2, 21, 2))
print(pares)

mult_tres = []
for n in range(3, 31, 3):
    mult_tres.append(n)
print(mult_tres)

cubos = []
for c in range(1, 11):
    cubos.append(c**3)
print(cubos)
    
cub = [c**3 for c in range(1, 11)]
print(cub)


