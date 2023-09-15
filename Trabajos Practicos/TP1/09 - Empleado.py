class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def aumentarSalario(self, aumento):
        self.salario *= aumento / 100 + 1
        return f"El salario del empleado {self.nombre} se incremento en {aumento}%"
    
    def cambiarCargo(self, nuevoCargo):
        self.cargo = nuevoCargo
        return f"El nuevo cargo del empleado {self.nombre} se cambio a {self.cargo}"
    
emp1 = Empleado("Carlos", 29, 2300, "Supervisor")
print(emp1.aumentarSalario(30))
print(emp1.cambiarCargo("Gerente"))