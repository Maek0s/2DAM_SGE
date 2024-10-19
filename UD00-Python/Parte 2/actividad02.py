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

contadorNumsBien = 0
contadorNumsMal = 0

with open('Sudoku2.in', 'r') as f:
    sudoku = [linea.split() for linea in f]

print("Sudoku introducido: ")
for line in sudoku:
    print(line)

for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        if (not esSudokuCorrecto(sudoku, i, j)):
            contadorNumsMal += 1
        else:
            contadorNumsBien += 1
        # Pruebas de cada numero: print(resultado, "- Number:", sudoku[i][j], " i:", i, "j:", j)

print("\nNumeros bien colocados:", contadorNumsBien)
print("Numero mal colocados:", contadorNumsMal)

if (contadorNumsMal > 0):
    print("\nIncorrecto.")
else:
    print("\nCorrecto.")