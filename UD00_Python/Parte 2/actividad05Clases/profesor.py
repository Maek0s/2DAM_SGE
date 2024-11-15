from actividad05Clases.tipoprofesor import TipoProfesor

class Profesor:
    def __init__(self, nombre, tipo):
        if not isinstance(tipo, TipoProfesor): # si no pones TipoProfesor.X dara error
            raise ValueError("El tipo de profesor debe ser un TipoProfesor")
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        # (ENUM) <name> = "<value>" | Ejemplo: CIENCIAS = "Ciencias"
        # tipo.name para el nombre del enum
        # tipo.value para el valor del enum
        return f"Nombre: {self.nombre} Tipo: ({self.tipo.value})"