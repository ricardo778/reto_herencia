# Primera clase padre
class ClaseA:
    def saludar(self):
        return "Hola desde ClaseA"

# Segunda clase padre
class ClaseB:
    def saludar(self):
        return "Hola desde ClaseB"

# Clase hija que hereda de ClaseA y ClaseB (herencia múltiple)
class ClaseC(ClaseA, ClaseB):
    pass

# Crear objeto de ClaseC
obj = ClaseC()

# Llamará al método de ClaseA porque está primero en el orden de herencia
print(obj.saludar())

# Muestra el orden de resolución de métodos (MRO)
print(ClaseC.mro())
