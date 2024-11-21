'''
Autor: Marcos Zahonero
Fecha: 21/11/2024
Descripción: Actividad 10, leer bar codes de una carpeta.
'''

from pyzbar.pyzbar import decode
from PIL import Image
import os

# Directorio con los barcodes
directorio = "actividad09Ficheros"

# Saca los archivos del directorio
with os.scandir(directorio) as archivos:
    print("\n==============================")
    for archivo in archivos:
        # Comprueba que es un .png y lee el codigo de barras
        if (archivo.name[-4:] == ".png"):
            # Abre la imagen
            imagen = Image.open(archivo)

            # Leer el código de barras
            codigos = decode(imagen)

            # Imprimir la información de cada código de barras
            for codigo in codigos:
                tipo = codigo.type
                datos = codigo.data.decode("utf-8")
                print(f"\nTipo de código: {tipo}")
                print(f"Datos del código: {datos}\n")
                # El nombre del archivo significa el alumno
                print(f"Nombre del alumno: {archivo.name[:-4]}")

                # La ID esta en el codigo de abajo quitando el 13º número
                print(f"ID del alumno: {int(datos[:-1])}")
                print("\n==============================")
