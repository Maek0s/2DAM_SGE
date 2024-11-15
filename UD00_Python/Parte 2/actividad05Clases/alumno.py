from actividad05Clases.profesor import Profesor

class Alumno:
    def __init__(self, nombre, curso, profesor):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor

    def __str__(self):
        return f"Nombre: {self.nombre} Curso: {self.curso} con Profesor: {self.profesor}"