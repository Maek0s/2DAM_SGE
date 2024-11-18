from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Crear la base de datos
Base = declarative_base()

# Crear la clase Profesor
class Profesor(Base):
    # Crear la tabla profesor
    __tablename__ = 'profesor'

    # Crear las columnas de la tabla profesor
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

    # Crear el constructor de la clase Profesor
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    # Crear el método __repr__ de la clase Profesor para hacer el print de un profesor
    def __repr__(self):
        return f'Profesor({self.id} - {self.nombre}, {self.tipo})'

# Crear la clase Alumno
class Alumno(Base):

    # Crear la tabla alumno
    __tablename__ = 'alumno'

    # Crear las columnas de la tabla alumno
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    curso = Column(String, nullable=False)
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    
    # Crear la relación entre la tabla alumno y la tabla profesor
    profesor = relationship("Profesor")

    # Crear el constructor de la clase Alumno
    def __init__(self, nombre, curso, profesor):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor

    # Crear el método __repr__ de la clase Alumno para hacer el print de un alumno
    def __repr__(self):
        return f'Alumno({self.id} - {self.nombre}, {self.curso}, ID: {self.profesor_id} [{self.profesor.nombre}] )'