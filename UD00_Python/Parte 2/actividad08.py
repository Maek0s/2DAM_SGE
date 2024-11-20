'''
Autor: Marcos Zahonero
Fecha: 19/11/2024
Descripción: Actividad 8, organizar archivos por su extensión en carpetas.
'''

import os
import shutil

# Colores para la terminal
negrita = "\033[1m"
reset = "\033[0m"

''' ¡EJECUTAR DESDE LA CARPETA PARTE 2 PARA SU CORRECTO FUNCIONAMIENTO! '''

# Borra las carpetas creadas
def resetCarpetas():
    for extension in extensiones:
        ruta = "actividad08Carpetas/" + extension
        if (os.path.exists(ruta)):
            shutil.rmtree(ruta)

# Crea las carpetas de cada extension en la lista
def crearCarpetas():
    for extension in extensiones:
        ruta = "actividad08Carpetas/" + extension
        if (not os.path.exists(ruta)):
            os.mkdir(ruta)

# Devuelve la extensión de un archivo
def sacarExtension(fichero):
    posPunto = fichero.rfind(".")
    return fichero[posPunto + 1::]

# Mueve los archivos a su carpeta correspondiente
def meterEnCarpeta():
    crearArchivos()
    crearCarpetas()

    # Lista de archivos en la carpeta
    contenidoCarpeta = os.listdir("actividad08Carpetas")

    for archivo in contenidoCarpeta:
        # Si es un archivo (miro si tiene "." o no)
        if (archivo.find(".") != -1):
            extension = sacarExtension(archivo)
            # Muevo el archivo a su carpeta correspondiente
            shutil.move(f"actividad08Carpetas/{archivo}",f"actividad08Carpetas/{extension}/{archivo}")
            print(f"El archivo \"{negrita}{archivo}{reset}\" se ha movido a la carpeta de {negrita}{extension}{reset}.")
        
# Crea los archivos de las extensiones
def crearArchivos():
    for extension in extensiones:
        # Si no existe el archivo, lo crea
        if (not os.path.exists("actividad08Carpetas/archivo." + extension)):
            open("actividad08Carpetas/archivo." + extension,"x")
    for extension in extensiones:
        if (not os.path.exists("actividad08Carpetas/archivo2." + extension)):
            open("actividad08Carpetas/archivo2." + extension,"x")

# Lista de extensiones
extensiones = ["png","mp4","doc"]

# Main #
if __name__ == "__main__":
    resetCarpetas()

    crearArchivos()
    meterEnCarpeta()