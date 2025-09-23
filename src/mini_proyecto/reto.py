print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializar atributos básicos
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        # Devolver información básica del producto
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock} unidades"
    
    def hay_stock(self):
        # Verificar si hay unidades disponibles
        return self.stock > 0


# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        # Inicializar atributo específico de Alimento
        self.fecha_caducidad = fecha_caducidad
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir fecha de caducidad
        return f"{super().mostrar_info()}, Caducidad: {self.fecha_caducidad}"


# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, precio, stock)
        # Inicializar atributo específico de Electronico
        self.garantia = garantia
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir información de garantía
        return f"{super().mostrar_info()}, Garantía: {self.garantia} meses"


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
p1 = Producto("Lapicero", 1500, 20)

# Crear una instancia de Alimento
a1 = Alimento("Leche", 3500, 10, "15/10/2025")

# Crear una instancia de Electronico
e1 = Electronico("Celular", 1200000, 5, 24)


print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
print(p1.mostrar_info())

# Mostrar información del alimento
print(a1.mostrar_info())

# Mostrar información del electrónico
print(e1.mostrar_info())


print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto
print(f"{p1.nombre} hay stock? {p1.hay_stock()}")
print(f"{a1.nombre} hay stock? {a1.hay_stock()}")
print(f"{e1.nombre} hay stock? {e1.hay_stock()}")
