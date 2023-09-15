class Pelicula:
    def __init__(self, titulo, director, duracion, genero):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion
        self.genero = genero
        
    def reproducir(self):
        return f"Se comenzo a reproducir {self.titulo} - Duración {self.duracion}"
        
    def recomendar(self, generoPreferido):
        if generoPreferido.casefold() == self.genero.casefold():
            return f"Seguro te gustaria ver {self.titulo}, del genero {self.genero}. Tu preferida."
        else:
            return f"La pelicula {self.titulo} no es de tu genero favorito"
            
rambo = Pelicula("Rambo: primera sangre", "Ted Kotcheff", 97, "Acción")

rambo.reproducir()
print(rambo.recomendar("Acción"))
print(rambo.recomendar("Drama"))