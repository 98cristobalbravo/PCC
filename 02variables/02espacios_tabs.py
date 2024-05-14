print("Python")
print("\tPython")
print("\t Python")
print("Lenguajes:\n \tPython\n \tJava\n \tJavascript\n \tC\n")

texto = "      python   "
print(texto)

texto = texto.rstrip()
print(texto)

texto = texto.lstrip()
print(texto)

textstrip = "  2  "
print(textstrip)
print(textstrip.strip())

# Remover prefijos
urlweb = "https://www.google.cl/?hl=es"
noprefix = urlweb.removeprefix("https://")
print(noprefix)
simpleurl_nosuffix = noprefix.removesuffix("/?hl=es")
print(simpleurl_nosuffix)