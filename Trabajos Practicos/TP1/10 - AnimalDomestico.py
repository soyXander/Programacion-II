class AnimalDomestico:
    def __init__(self, nombre, especie, edad, dueño):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.dueño = dueño
        
    def sonido(self):
        if self.especie.casefold() == "perro":
            return "Woof woof"
        elif self.especie.casefold() == "gatos":
            return "Meow meow"
        else:
            return "Sonido caracteristico del animal no registrado"
    
    def verificarEdad(self):
        if self.especie.casefold() == "perro":
            if self.edad > 84:
                return "El perro es anciano"
            elif self.edad > 12:
                return "El perro es adulto"
            else:
                return "El perro es joven"
        elif self.especie.casefold() == "gatos":
            if self.edad > 180:
                return "El gato es anciano"
            elif self.edad > 84:
                return "El gato es adulto"
            else:
                return "El gato es joven"
        else:
            return "No hay registros de edad para esta especie"
        
mora = AnimalDomestico("Mora", "Perro", 18, "Fer")
print(mora.sonido())
print(mora.verificarEdad())
