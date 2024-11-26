'''
Autor: Marcos Zahonero
Fecha: 23/11/2024
Descripción: Solución para el problema de las 8 reinas usando backtracking.
Comentario: El código inicial es mio y todo, pero a la hora de la función
resolverReinas() me base en el código de un video de YT que lo hacia en java, adjunto el link
ya que no encontraba la solución de averiguarlo, y se basaba en la recursividad.
Vídeo: https://www.youtube.com/watch?v=s7kBjMOMWg0
'''

def checkDiagonales(i, j, tablero, tamanyo):
    # Comprobamos hacia arriba izquierda
    x, y = i, j
    while x >= 0 and y >= 0:
        if tablero[x][y] == "X":
            return False
        x -= 1
        y -= 1

    # Comprobamos hacia arriba derecha
    x, y = i, j
    while x >= 0 and y < tamanyo:
        if tablero[x][y] == "X":
            return False
        x -= 1
        y += 1

    return True

def checkRectas(i, j, tablero, tamanyo):
    # Comprobamos hacia arriba
    for x in range(i):
        if tablero[x][j] == "X":
            return False
    return True

def esPosicionSegura(i, j, tablero, tamanyo):
    if (checkRectas(i, j, tablero, tamanyo) == False):
        return False
    if (checkDiagonales(i, j, tablero, tamanyo) == False):
        return False
    
    return True
    #return checkRectas(i, j, tablero, tamanyo) and checkDiagonales(i, j, tablero, tamanyo)

def crearTablero(tamanyo):
    return [["0" for _ in range(tamanyo)] for _ in range(tamanyo)]

def mostrarTablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

# Esto es una función recursiva que se llama a sí misma
def resolverReinas(tablero, fila, tamanyo, soluciones):
    if fila == tamanyo:  # Si se han colocado todas las reinas
        soluciones.append([fila[:] for fila in tablero])
        return
    
    for columna in range(tamanyo):
        if esPosicionSegura(fila, columna, tablero, tamanyo):
            tablero[fila][columna] = "X"  # Coloca la reina
            resolverReinas(tablero, fila + 1, tamanyo, soluciones)
            tablero[fila][columna] = "0"  # Retira la reina para probar otra opción

if __name__ == '__main__':
    tamanyo = 4 # Para evitar error lo dejo por default a 4 aunque despues lo cambias
    soluciones = [] # Lista para guardar las soluciones
    tablero = crearTablero(tamanyo)
    opcion = 0

    while opcion != -1:
        print("\n- = El problema de las 8 reinas = -")
    
        print("\nIntroduce 4 al 11 para ejecutar el problema dando el valor n")
        print("El valor n es el tamaño del tablero nxn y el num de reinas por colocar.")
        print("Introduce -1 para salir")
        opcion = int(input("\nIntroduce una opción: "))

        if (opcion >= 4 and opcion <= 11):
            tamanyo = opcion
            tablero = crearTablero(tamanyo)
            soluciones = []
            resolverReinas(tablero, 0, tamanyo, soluciones)
            print(f"Se han encontrado {len(soluciones)} soluciones para el problema de las {tamanyo} reinas:\n")

            i = 0
            for solucion in soluciones:
                i += 1
                print(f"Solución {i}:")
                mostrarTablero(solucion)
        elif opcion == -1:
            break
        else:
            print("Opción no válida")