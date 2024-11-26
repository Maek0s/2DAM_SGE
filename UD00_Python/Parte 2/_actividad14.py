'''
Autor: Marcos Zahonero
Fecha: 23/11/2024
Descripción: Actividad 14, el problema de las 8 reinas.
'''

def checkDiagonales(i, j, tablero, tamanyo):
    iReal = i
    jReal = j

    # Comprobamos hacia arriba izquierda
    while i > 0 and j > 0:
        i -= 1
        j -= 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    i = iReal
    j = jReal

    # Comprobamos hacia arriba derecha
    while i > 0 and j < tamanyo - 1:
        i -= 1
        j += 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    i = iReal
    j = jReal

    # Comprobamos hacia abajo izquierda
    while i < tamanyo - 1 and j > 0:
        i += 1
        j -= 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    i = iReal
    j = jReal

    # Comprobamos hacia abajo derecha
    while i < tamanyo - 1 and j < tamanyo - 1:
        i += 1
        j += 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    return True

def checkRectas(i, j, tablero, tamanyo):
    iReal = i
    jReal = j

    # Comprobamos hacia arriba
    while i > 0:
        i -= 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    i = iReal

    # Comprobamos hacia abajo
    while i < tamanyo - 1:
        i += 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    i = iReal

    # Comprobamos hacia la izquierda
    while j > 0:
        j -= 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    j = jReal

    # Comprobamos hacia la derecha
    while j < tamanyo - 1:
        j += 1
        if tablero[i][j] == "X" or tablero[i][j] == ".":
            return False

    return True

def crearTablero(tamanyo):
    return [["0" for _ in range(tamanyo)] for _ in range(tamanyo)]

def mostrarTablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

if __name__ == '__main__':
    numSoluciones = 0
    tamanyo = 5
    soluciones = []
    colocadas = 0
    iniciosUsados = ""
    iteracion = 0

    tablero = crearTablero(tamanyo)

    while numSoluciones < 10:
        tablero = crearTablero(tamanyo)
        colocadas = 0

        if (iteracion > 1000):
            print("No se han encontrado más soluciones")
            break

        for i in range(tamanyo):
            for j in range(tamanyo):
                if checkRectas(i, j, tablero, tamanyo):
                    print(f"Rectas ok en ({i}, {j})")
                    if checkDiagonales(i, j, tablero, tamanyo):
                        print(f"Diagonales ok en ({i}, {j})")
                        
                        if f"{i}, {j}" in iniciosUsados:
                            print(f"{iteracion}. Ya se ha colocado una reina en ({i}, {j}) en un intento fallido anterior, sols: {numSoluciones}")
                            mostrarTablero(tablero)
                            continue

                        if colocadas == 0:
                            iniciosUsados += f"{i}, {j} "

                        tablero[i][j] = "X"
                        colocadas += 1
                        mostrarTablero(tablero)
                        break

        iteracion += 1
        mostrarTablero(tablero)

        if colocadas == tamanyo:
            numSoluciones += 1
            soluciones.append(tablero)
            colocadas = 0
            print("Solución encontrada:")
            mostrarTablero(tablero)
    
    print(f"Se han encontrado {numSoluciones} soluciones:\n")

    for solucion in soluciones:
        mostrarTablero(solucion)