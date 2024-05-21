"""
for i in range(1, 5):
    x = i
    piramide = ("#" * x)
    print(piramide)
"""
altura = 5
for i in range(1, altura):
    num_espacios = altura - i
    espacio = "-" * num_espacios
    print(f"{espacio}{"#" * i}")