class Escuela:
    def __init__(self, nombre, localidad, responsable, profesores, alumnos):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.profesores = profesores
        self.alumnos = alumnos

    # Agregar a listas #
    
    def agregar_profesor(self, profesor):
        print("Agregando profesor con nombre " + profesor.nombre + " y tipo profesor " + profesor.tipo.value)
        self.profesores.append(profesor)

    def agregar_alumno(self, alumno):
        print("Agregando alumno con nombre " + alumno.nombre + " y curso " + alumno.curso)
        self.alumnos.append(alumno)

    # Getters #

    def obtener_profesores(self):
        return self.profesores
    
    def obtener_alumnos(self):
        return self.alumnos

    # Prints #

    def mostrar_profesores(self):
        for profesor in self.profesores:
            print(profesor)

    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno)
