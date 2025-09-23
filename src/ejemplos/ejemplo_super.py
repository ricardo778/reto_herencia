# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Clase hija
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # super() llama al constructor de Vehiculo
        super().__init__(marca, modelo)
        self.puertas = puertas

# Crear objeto de Automovil
auto = Automovil("Mazda", "CX-5", 5)
# Accedemos a todos los atributos heredados y nuevos
print(auto.marca, auto.modelo, auto.puertas)
