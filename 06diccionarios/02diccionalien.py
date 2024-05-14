alien_0 = {"posicion_x": 0, 
           "posicion_y": 25,
           "velocidad": "media"}

# mover alien a la izquierda

if alien_0["velocidad"] == "lenta":
    aumentar_x = 1
elif alien_0["velocidad"] == "media":
    aumentar_x = 2
else:
    aumentar_x = 3
    
# nueva posicion = antigua posicion + aumentar segun velocidad

alien_0["posicion_x"] = alien_0["posicion_x"] + aumentar_x
print(f"La nueva posicion es {alien_0['posicion_x']}")

alien_0["color"] = "rojo"
print(alien_0)

del alien_0["color"]
print(alien_0)