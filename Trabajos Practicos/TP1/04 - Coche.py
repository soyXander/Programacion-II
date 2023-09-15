class Coche:
    def __init__(self, marca, modelo, año, velocidad_actual = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_actual = velocidad_actual
        
    def acelerar(self, velocidad = 1):
        self.velocidad_actual += velocidad
        
    def frenar(self, velocidad = 1):
        if self.velocidad_actual > 0 and velocidad < self.velocidad_actual:
            self.velocidad_actual -= velocidad
        else:
            self.velocidad_actual = 0

audi = Coche("Audi", "A5", 2014, 120)
print(audi.velocidad_actual)
audi.acelerar(10);
print(audi.velocidad_actual)
audi.frenar(200)
print(audi.velocidad_actual)
