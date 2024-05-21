sin_verificar = ["juan", "pepita", "carlita", "nardita"]
verificado = []

while sin_verificar:
    usuario_actual = sin_verificar.pop()
    print(sin_verificar)

    resultado = verificado.append(usuario_actual)
    print(resultado)
    
print(sin_verificar)
print(verificado)