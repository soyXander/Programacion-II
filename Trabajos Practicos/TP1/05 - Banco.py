class Banco:
    def __init__(self, nombre, saldoTotal, tazasInteres):
        self.nombre = nombre
        self.saldoTotal = saldoTotal
        self.tazasInteres = tazasInteres
        self.clientes = []
    
    def abrirCuenta(self, nombre, apellido, dni, saldoActual = 0):
        cliente = Cliente(nombre, apellido, dni, saldoActual)
        self.clientes.append(cliente)
        self.saldoTotal += saldoActual

class Cliente:
    def __init__(self, nombre, apellido, dni, saldoActual):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.saldoActual = saldoActual
    
    def __str__(self):
        return f"Cliente: {self.apellido}, {self.nombre} (DNI: {self.dni}) - Saldo Actual: ${self.saldoActual}"
    
b = Banco("Santander", 0, 1.1)
b.abrirCuenta("Gabriel", "Romero", 33123456, 100)