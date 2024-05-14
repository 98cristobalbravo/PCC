lenguajes = {
    "jen": "python",
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
    }

print(lenguajes["jen"].title())
# print(lenguajes["jenn"])

jenn = lenguajes.get("jenn", "Key no encontrada en diccionario")
print(jenn)
print(lenguajes.get("jenn"))