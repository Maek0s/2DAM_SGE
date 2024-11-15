'''
Autor: Marcos Zahonero
Fecha: 19/10/2024
Descripción: Actividad 4, comprobación de campo de minas.
'''

# falta pillar la string y meterla en lista

def contandoCampo(miCampo, i, j):
    contador = 0

    if (miCampo[i][j] == "-1"):
        return -1
    
    # ↖️ Hacia arriba izquierda
    if (i > 0 and j > 0):
        if (miCampo[i - 1][j - 1] == "-1"):
            # print(i,j, "arriba izquierda")
            contador += 1
    
    # ⬆️ Hacia arriba
    if (i > 0):
        if (miCampo[i - 1][j] == "-1"):
            # print(i,j, "arriba")
            contador += 1

    # ↗️ Hacia arriba derecha
    if (i > 0 and j < len(miCampo)):
        if (miCampo[i - 1][j + 1] == "-1"):
            # print(i,j, "arriba derecha")
            contador += 1

    # ➡️ Hacia derecha
    if (j < len(miCampo[i]) - 1):
        if (miCampo[i][j + 1] == "-1"):
            # print(i,j, "derecha")
            contador += 1

    # ↘️ Hacia abajo derecha
    if (i < len(miCampo) - 1 and j < len(miCampo[i]) - 1):
        if (miCampo[i + 1][j + 1] == "-1"):
            # print(i,j, "abajo derecha")
            contador += 1

    # ⬇️ Hacia abajo
    if (i < len(miCampo) - 1):
        if (miCampo[i + 1][j] == "-1"):
            # print(i,j, "abajo")
            contador += 1
    
    # ↙️ Hacia abajo izquierda
    if (i < len(miCampo) - 1 and j > 0):
        if (miCampo[i + 1][j - 1] == "-1"):
            # print(i,j, "abajo izq.")
            contador += 1

    # ⬅️ Hacia izquierda
    if (j > 0):
        if (miCampo[i][j - 1] == "-1"):
            # print(i,j, "izq.")
            contador += 1

    return contador

def obtener_campo(filas):
    campo = []
    for i in range(filas):
        fila = input().split()
        campo.append(fila)
    return campo

miCampo = obtener_campo(2) # Aquí indicas las filas que soportará el campo
# Las columnas debes respetar la primera decisión y no hacer menos columnas en una que otra

buscaMinas = [
        ["0" for _ in range(len(miCampo[0]))]
        for _ in range(len(miCampo))
    ]

for i in range(len(miCampo)):
    for j in range(len(miCampo[i])):
        buscaMinas[i][j] = contandoCampo(miCampo, i, j)

print("\nResultado: ")

for i in range(len(buscaMinas)):
    for j in range(len(buscaMinas[i])):
        print(buscaMinas[i][j],end=" ")
    print()