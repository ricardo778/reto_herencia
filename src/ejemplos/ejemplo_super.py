class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")

    def detener(self):
        print(f"El vehículo {self.marca} {self.modelo} se detiene.")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numero_puertas):
        # Aquí usamos super() para llamar al __init__ de Vehiculo
        super().__init__(marca, modelo)
        self.numero_puertas = numero_puertas

    def abrir_puertas(self):
        print(f"El automóvil {self.marca} {self.modelo} tiene {self.numero_puertas} puertas y se abren.")

    # Sobrescritura de método
    def detener(self):
        # Podemos usar también super().detener() si queremos combinar comportamientos
        print(f"El automóvil {self.marca} {self.modelo} está frenando suavemente.")


auto = Automovil("Toyota", "Corolla", 4)
auto.arrancar()       # Viene de Vehiculo
auto.abrir_puertas()
auto.detener()        # usa la versión de Automovil, no la de Vehiculo
