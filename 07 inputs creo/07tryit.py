sandwich_pedidos = ["pan y pollo", "carne y palta", "vegano"]
sandwich_terminados = []

while sandwich_pedidos:
    sandwich_actual = sandwich_pedidos.pop()    
    sandwich_terminados.append(sandwich_actual)

print("--- Pedidos terminados ---")
for i in sandwich_terminados:
    print(f"\t{i}")