'''
Autor: Marcos Zahonero
Fecha: 15/11/2024
Descripción: Actividad 5, organizar una escuela con varias Clases (Escuela, Profesor y Alumno).
'''

from actividad05Clases.escuela import Escuela
from actividad05Clases.profesor import Profesor
from actividad05Clases.alumno import Alumno
from actividad05Clases.tipoprofesor import TipoProfesor

if __name__ == "__main__":
    profesor1 = Profesor("Pepe", TipoProfesor.CIENCIAS)
    profesor2 = Profesor("Ana", TipoProfesor.LETRAS)
    profesor3 = Profesor("Luis", TipoProfesor.MIXTO)
    profesor4 = Profesor("Maria", TipoProfesor.CIENCIAS)

    profesores = [profesor1, profesor2, profesor3, profesor4]

    alumno1 = Alumno("Juan", "1º ESO", profesor1)
    alumno2 = Alumno("Pedro", "2º ESO", profesor2)
    alumno3 = Alumno("Sara", "3º ESO", profesor3)
    alumno4 = Alumno("Paco", "4º ESO", profesor4)

    alumnos = [alumno1, alumno2, alumno3, alumno4]

    escuela1 = Escuela("Colegio 1", "Madrid", "Pepe", profesores, alumnos)

    # Mostrar profesores y alumnos

    print("# Profesores y alumnos sin añadir profesor5 y alumno5 #\n")

    print("- Profesores -")
    escuela1.mostrar_profesores()
    
    print("\n- Alumnos -")
    escuela1.mostrar_alumnos()

    # Agregar profesor y alumno

    print("\n# Añadiendo profesor5 y alumno5 #\n")

    profesor5 = Profesor("Rosa", TipoProfesor.LETRAS)
    escuela1.agregar_profesor(profesor5)

    alumno5 = Alumno("Lola", "5º ESO", profesor5)
    escuela1.agregar_alumno(alumno5)

    # Mostrar profesores y alumnos

    print("\n# Profesores y alumnos con profesor5 y alumno5 añadidos #\n")

    print("- Profesores -")
    escuela1.mostrar_profesores()
    
    print("\n- Alumnos -")
    escuela1.mostrar_alumnos()


