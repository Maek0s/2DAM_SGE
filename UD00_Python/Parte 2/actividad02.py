'''
Autor: Marcos Zahonero
Fecha: 19/10/2024
Descripción: Actividad 2, comprobación de un sudoku con toque personal.
Extra: He añadido un menu para listar los archivos de la carpeta y elegir uno
así podrás poner tu propios sudokus y elegirlos cuando quieras.
'''
import os

def esSudokuCorrecto(sudoku, i, j):
    tempI = i
    tempJ = j
    element = sudoku[i][j]

    # Hacia arriba
    while (i > 0):
        i = i - 1
        if (i > 0):
            if (element == sudoku[i][j]):
                return False
    i = tempI

    # Hacia abajo
    while (i < len(sudoku)):
        i = i + 1
        if (i < len(sudoku)):
            if (element == sudoku[i][j]):
                return False
    i = tempI

    # Hacia izquierda
    while (j > 0):
        j = j - 1
        if (j > 0):
            if (element == sudoku[i][j]):
                return False
    j = tempJ

    # Hacia derecha
    while (j < len(sudoku[i]) - 1):
        if (j < len(sudoku[i]) - 1):
            j = j + 1
            if (element == sudoku[i][j]):
                return False

    return True



def listar_archivos(carpeta):
    try:
        archivos = [f for f in os.listdir(carpeta) if os.path.isfile(os.path.join(carpeta, f))]
        return archivos
    except FileNotFoundError:
        print("No se ha encontrado la carpeta. Comprueba que estés en la carpeta correcta.")
        return []

if __name__ == "__main__":
    contadorNumsBien = 0
    contadorNumsMal = 0

    carpeta = "actividad02Sudokus" # Carpeta donde se encuentran los sudokus
    archivos = listar_archivos(carpeta) # Lista de archivos en la carpeta

    if not archivos:
        print("No hay archivos en la carpeta.")
        print("Tu carpeta es: " + carpeta + " comprueba que hayan archivos en ella y que estas en una buena ruta.")
        exit()

    print(f"¡Archivos encontrados en la carpeta \"{carpeta}\"!\n") # Mensaje de archivos encontrados

    print("Archivos disponibles:")
    for i, archivo in enumerate(archivos): # Enumerar los archivos
        print(f"{i + 1}. {archivo}")

    try:
        opcion = int(input("\nElige un archivo por su número: ")) - 1 # Elegir un archivo
        if opcion < 0 or opcion >= len(archivos):
            print("Opción no válida.")
            
    except ValueError:
        print("Entrada no válida.")
        exit()

    sudokuElegido = carpeta + "/" + archivos[opcion] # Ruta con la carpeta y el sudoku elegido
    print(f"Has elegido {sudokuElegido}")

    try:
        with open(sudokuElegido, "r") as f: # Abre el archivo
            sudoku = [linea.split() for linea in f]
    except FileNotFoundError:
        print("No se ha encontrado el archivo. Comprueba que estes en la carpeta \"Parte 2\" sino no funciona.")
    except Exception as e:
        print("Error:", e)

    print("Sudoku introducido: ")
    for line in sudoku:
        print(line)

    for i in range(len(sudoku)):
        for j in range(len(sudoku[i])):
            if (not esSudokuCorrecto(sudoku, i, j)):
                contadorNumsMal += 1
            else:
                contadorNumsBien += 1
            # Pruebas de cada numero para el debug
            # print(esSudokuCorrecto(sudoku, i, j), "- Number:", sudoku[i][j], " i:", i, "j:", j)

    print("\nNumeros bien colocados:", contadorNumsBien)
    print("Numero mal colocados:", contadorNumsMal)

    if (contadorNumsMal > 0):
        print("\nIncorrecto.")
    else:
        print("\nCorrecto.")