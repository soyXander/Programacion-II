class Libro:
    def __init__(self, titulo, autor, año, disponible):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = disponible
        
    def solicitar_prestamo(self):
        if self.disponible == True:
            self.disponible = False
            return "El libro se presto correctamente"
        else: 
            return "Lo sentimos el libro ya se encuentra prestado"
            
    def devolver_libro(self, dias):
        if self.disponible == False:
            if dias > 7:
                return f"Multa de $100 por retraso de {dias} días en la devolución"
            else:
                return "El libro a sido devuelto"
        else:
            return "No se puede devolver un libro que no fue prestado"
        
elSecreto = Libro("El secreto", "Rhonda Byrne", 2006, True)
elSecreto.solicitar_prestamo()
elSecreto.devolver_libro(8)