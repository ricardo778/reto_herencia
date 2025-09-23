# Clase padre
class Animal:
    def hablar(self):
        return "Este animal hace un sonido"

# Clase hija que sobrescribe hablar()
class Perro(Animal):
    def hablar(self):
        return "Guau!"

# Otra clase hija que sobrescribe hablar()
class Gato(Animal):
    def hablar(self):
        return "Miau!"

# Lista de objetos de diferentes tipos
animales = [Perro(), Gato(), Animal()]

# Polimorfismo: cada objeto responde con su propia implementación
for a in animales:
    print(a.hablar())
