print("=== PROGRAMA: JERARQUÍA DE PRODUCTOS ===\n")

# Clase base Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializar atributos básicos
        # Escribe aquí tu código
        
        
        
    
    def mostrar_info(self):
        # Devolver información básica del producto
        # Escribe aquí tu código
        
    
    def hay_stock(self):
        # Verificar si hay unidades disponibles
        # Escribe aquí tu código
        

# Clase Alimento que hereda de Producto
class Alimento(Producto):
    def __init__(self, nombre, precio, stock, fecha_caducidad):
        # Llamar al constructor de la clase padre
        # Escribe aquí tu código
        
        # Inicializar atributo específico de Alimento
        # Escribe aquí tu código
        
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir fecha de caducidad
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        


# Clase Electronico que hereda de Producto
class Electronico(Producto):
    def __init__(self, nombre, precio, stock, garantia):
        # Llamar al constructor de la clase padre
        # Escribe aquí tu código
        
        # Inicializar atributo específico de Electronico
        # Escribe aquí tu código
        
    
    def mostrar_info(self):
        # Sobreescribir el método para incluir información de garantía
        # Escribe aquí tu código (puedes usar super() o reimplementar)
        


# === CREACIÓN Y PRUEBA DE INSTANCIAS ===
print("=== CREANDO PRODUCTOS ===")

# Crear una instancia de Producto genérico
# Escribe aquí tu código


# Crear una instancia de Alimento
# Escribe aquí tu código


# Crear una instancia de Electronico
# Escribe aquí tu código


print("\n=== INFORMACIÓN DE PRODUCTOS ===")

# Mostrar información del producto genérico
# Escribe aquí tu código


# Mostrar información del alimento
# Escribe aquí tu código


# Mostrar información del electrónico
# Escribe aquí tu código


print("\n=== VERIFICANDO STOCK ===")

# Verificar stock de cada producto
# Escribe aquí tu código
