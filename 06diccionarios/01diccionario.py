alien_0 = {
    "color": "verde",
    "puntos": 5
}

print(alien_0['color'])
print(alien_0['puntos'])

nuevos_puntos = alien_0["puntos"]
print(f"Acabas de ganar {nuevos_puntos} puntos!")

alien_0["x_posicion"] = 0
alien_0["y_posicion"] = 25

print(alien_0)

alien_uno = {}
alien_uno["color"] = "rojo"
alien_uno["puntos"] = 10

print(alien_uno)
alien_uno["color"] = "amarillo"
print(alien_uno)