def describir_animal( animal_nombre: str, animal_tipo: str = "perro"):
    print(f"\nTengo un {animal_tipo}")
    print(f"Su nombre es, '{animal_nombre.title()}'")

describir_animal("gato", "sirius")
describir_animal("perro", "kika")

# Keywords
describir_animal(animal_tipo="Caballo", animal_nombre="tarde pero llega")

describir_animal(animal_nombre= "Charrua")