'''
Autor: Marcos Zahonero
Fecha: 19/11/2024
Descripción: Actividad 15, realizar cambios en tu portapapeles con Pyperclip.
'''
import pyperclip

# Debes copiar algo en tu portapapeles como "hola Oscar viva PYthOn" y al ejecutarlo y luego pegarlo se habra transformado
frase = pyperclip.paste()

palabrasProhibidas = []

# ¡IMPORTANTE ESTAR EJECUTANDO ESTO DESDE CARPETA "PARTE 2"!
# Abrimos el archivo llista.txt para sacar las palabras prohibidas
with open("actividad15Listas/llista.txt","r") as f:
    for linea in f:
        palabrasProhibidas.append(linea.replace("\n","").upper())

resultado = ""

# Dividimos la frase por espacios
palabras = frase.split(" ")

# Miramos las palabras convirtiendolas en mayusculas para evitar la distintincion de mayusculas y si esta prohbida
# multiplicamos su longitud a "*" y se añade al texto y sino se añade la palabra
for palabra in palabras:
    if palabra.upper() in palabrasProhibidas:
        resultado += "*" * len(palabra) + " "
    else:
        resultado += palabra + " "

# Printeamos el resultado para algo mas visual pero lo volvemos a dejar en el portapapeles como pedia
print(resultado)
pyperclip.copy(resultado)