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


miCampo = [["0", "0", "-1", "0"],
           ["0", "-1", "-1", "0"]]

buscaMinas = [["0", "0", "0", "0"],
           ["0", "0", "0", "0"]]

for i in range(len(miCampo)):
    for j in range(len(miCampo[i])):
        buscaMinas[i][j] = contandoCampo(miCampo, i, j)

print("\nResultado: ")

for i in range(len(buscaMinas)):
    for j in range(len(buscaMinas[i])):
        print(buscaMinas[i][j],end=" ")
    print()