'''
Autor: Marcos Zahonero
Fecha: 21/11/2024
Descripción: Actividad 9, pasar un .csv a un codigo de barras.
'''

# Librerias necesarias
import csv
from barcode.writer import ImageWriter
import barcode

fileCSV = "actividad09Ficheros/alumnos.csv"

# Clase de código de barras EAN13 (requiere 12 dígitos, el dígito 13 se calcula automáticamente)
ean13 = barcode.get_barcode_class('ean13')

# Lee el archivo CSV y genera los códigos de barras
with open(fileCSV, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        nombre, id_alumno = row
        
        # Asegúrate de que el ID tiene 12 caracteres (EAN-13 requiere exactamente 12 dígitos)
        id_alumno = id_alumno.zfill(12)

        # Genera el código de barras
        codigo_barras = ean13(id_alumno, writer=ImageWriter())
        
        codigo_barras.save(f"actividad09Ficheros/{nombre}")
        print(f"Código de barras generado para {nombre} y guardado en actividad09Ficheros/{nombre}")