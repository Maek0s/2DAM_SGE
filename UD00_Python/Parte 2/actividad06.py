'''
Autor: Marcos Zahonero
Fecha: 18/11/2024
Descripción: Actividad 6, bases de datos en Python.
'''

from actividad06DB.db import session
from actividad06DB.models import Profesor, Alumno

def run():
    # Borrar datos de la base de datos para evitar duplicar datos
    session.query(Profesor).delete()
    session.query(Alumno).delete()

    # Crear profesores
    profesor1 = Profesor("Pepe", "Ciencias")
    profesor2 = Profesor("Ana", "Letras")
    profesor3 = Profesor("Luis", "Mixto")
    profesor4 = Profesor("Maria", "Ciencias")
    session.add_all([profesor1, profesor2, profesor3, profesor4])
    session.commit()

    # Crear alumnos
    alumno1 = Alumno("Juan", "1º ESO", profesor1)
    alumno2 = Alumno("Pedro", "2º ESO", profesor2)
    alumno3 = Alumno("Sara", "3º ESO", profesor3)
    alumno4 = Alumno("Paco", "4º ESO", profesor4)
    session.add_all([alumno1, alumno2, alumno3, alumno4])
    session.commit()

    # Mostrar profesores y alumnos
    print("\n# Profesores y alumnos sin añadir profesor5 y alumno5 #\n")

    print("- Profesores -")
    profesores = session.query(Profesor).all()
    for profesor in profesores:
        print(profesor)
    
    print("\n- Alumnos -")
    alumnos = session.query(Alumno).all()
    for alumno in alumnos:
        print(alumno)

    # Agregar profesor y alumno
    print("\n# Añadiendo profesor5 y alumno5 #\n")

    profesor5 = Profesor("Rosa", "Letras")
    session.add(profesor5)
    session.commit()

    alumno5 = Alumno("Lola", "5º ESO", profesor5)
    session.add(alumno5)
    session.commit()

    # Mostrar profesores y alumnos
    print("\n# Profesores y alumnos con profesor5 y alumno5 añadidos #\n")

    print("- Profesores -")
    profesores = session.query(Profesor).all()
    for profesor in profesores:
        print(profesor)
    
    print("\n- Alumnos -")
    alumnos = session.query(Alumno).all()
    for alumno in alumnos:
        print(alumno)

# Iniciar la aplicación
if __name__ == '__main__':
    run()