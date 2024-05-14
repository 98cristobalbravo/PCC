"""
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

print(aliens)
"""

aliens = []

for alien in range(30):
    nuevo_alien = {'color': 'verde', 'puntos': 5, 'velocidad': 'lento'}
    aliens.append(nuevo_alien)

# mostrar 5 aliens

for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Numero total de aliens creados: {len(aliens)}")