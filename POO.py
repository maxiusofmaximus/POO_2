# Definición de la primera superclase Empleados
class Empleados:
    def __init__(self):
        self.nombre = ""
    
    def pedir_nombre(self):
        self.nombre = input("Ingrese el nombre del empleado: ")

# Definición de la segunda superclase Salario
class Salario:
    def __init__(self):
        self.salario = 0.0
    
    def pedir_salario(self):
        self.salario = float(input("Ingrese el salario del empleado: "))

# Definición de la subclase Designacion que hereda de Empleados y Salario
class Designacion(Empleados, Salario):
    def __init__(self):
        Empleados.__init__(self)
        Salario.__init__(self)
        self.cargo = ""
    
    def pedir_cargo(self):
        self.cargo = input("Ingrese el cargo del empleado: ")

# Instanciando un objeto de la clase Designacion
empleado = Designacion()

# Verificando si el objeto tiene los métodos necesarios
empleado.pedir_nombre()
empleado.pedir_salario()
empleado.pedir_cargo()

# Mostrando la información recolectada
print(f"Nombre del empleado: {empleado.nombre}")
print(f"Salario del empleado: {empleado.salario}")
print(f"Cargo del empleado: {empleado.cargo}")
