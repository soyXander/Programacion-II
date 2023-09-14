class Estudiante:
    def __init__(self, nombre, edad, promedio, carrera):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        self.carrera = carrera
        
    def verificar_aprobacion(self):
        if self.promedio >= 70:
            return "Aprobado"
        else:
            return "Reprobado"
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
alumno = Estudiante("Gabriel Humerez Romero", 30, 80, "Tec. en programación")
print(alumno.verificar_aprobacion())
print(alumno.es_mayor_de_edad())