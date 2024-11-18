'''
Autor: Marcos Zahonero
Fecha: 17/11/2024
Descripción: Actividad 12, lee una imagen y la convierte a texto.
'''

from PIL import Image
import pytesseract

# Ruta del ejecutable de Tesseract (Solo me funcionará a mi con esto)
# tendrás que cambiarlo o ejecutarlo en virtualenv
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Maek0s\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Abre la imagen
img = Image.open("actividad12Imagen/imagen.png")
# Convierte la imagen a texto
result = pytesseract.image_to_string(img)

# Escribe el resultado en un archivo y lo printea por consola
with open("actividad12Imagen/resultado.txt", mode ="w") as file:
    file.write(result)
    print("Hecho!\nTexto:\n")
    print(result)
    