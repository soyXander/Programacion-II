class Restaurante:
    def __init__(self, nombre, tipoCocina, cantMesasDisponibles):
        self.nombre = nombre
        self.tipoCocina = tipoCocina
        self.cantMesasDisponibles = cantMesasDisponibles
        self.valoracion = 0
        
    def reservar(self, cantMesas = 1):
        if cantMesas > 0 and cantMesas <= self.cantMesasDisponibles:
            self.cantMesasDisponibles -= cantMesas
            return f"Se realizo correctamente la reserva de {cantMesas} mesas en {self.nombre}"
        else:
            return f"No hay mesas disponibles parar reservar en {self.nombre}"
    
    def calificar(self, valoracion):
        if valoracion >= 1 and valoracion <= 5:
            self.valoracion = valoracion
            return f"La nueva calificacion de {self.nombre} es de {self.valoracion}"
        else:
            return "La valoracion tiene que ser entre 1 y 5"
            
mostaza = Restaurante("Mostaza", "Rapida", 10)
print(mostaza.reservar(2))
print(mostaza.calificar(4.3))