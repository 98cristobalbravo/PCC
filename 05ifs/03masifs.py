edad = 13

if edad >= 18:
    print(f"Puedes votar")
else:
    print(f"No puedes votar")
    

if edad < 4:
    print("Ingreso gratuito")
elif edad < 18:
    print("Valor entrada: 25")
else:
    print("Precio entrada: 40")
    

age = 12

if age < 4:
   price = 0
elif age < 18:
    price = 25
else:
    price = 40
    
print(f"El valor de entrada es {price}")

ingredientes = ["hongos", "extra queso"]

if "hongos" in ingredientes:
    print("hngos añadidos")
if "carne" in ingredientes:
    print("carne agregada")
if "extra queso" in ingredientes:
    print("extra queso agregado")