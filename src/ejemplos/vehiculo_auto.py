# Clase padre
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método de la clase padre
    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Clase hija que hereda de Vehiculo
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # super() llama al constructor de la clase padre
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Sobrescritura del método descripcion()
    def descripcion(self):
        return f"{super().descripcion()}, Puertas: {self.puertas}"

# Crear un objeto de Automovil
auto = Automovil("Toyota", "Corolla", 4)
print(auto.descripcion())  # Muestra la descripción completa
