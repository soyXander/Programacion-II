class Coche:
    def __init__(self, marca, modelo, año, velocidad_actual = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_actual = velocidad_actual
        
    def acelerar(self, velocidad):
        self.velocidad_actual += velocidad
        
    def frenar(self, velocidad):
        if self.velocidad_actual > 0 and velocidad < self.velocidad_actual:
            self.velocidad_actual -= velocidad
        else:
            self.velocidad_actual = 0

c = Coche("Audi", "A5", 2014, 120)
print(c.velocidad_actual)
c.acelerar(10);
print(c.velocidad_actual)
c.frenar(200)
print(c.velocidad_actual)
