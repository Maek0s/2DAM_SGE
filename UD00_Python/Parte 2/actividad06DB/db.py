from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear el motor de la base de datos
engine = create_engine('sqlite:///actividad06DB/escuela.sqlite')

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear la base declarativa
from actividad06DB.models import Base
Base.metadata.create_all(engine)