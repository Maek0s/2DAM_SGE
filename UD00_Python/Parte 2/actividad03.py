'''
Autor: Marcos Zahonero
Fecha: 18/11/2024
Descripción: Actividad 3, identificar el número de patrones.
'''

def numeroPatrones(text):
    # Lista de patrones a buscar
    listasPatrones = ["00","101","ABC","HO"]

    # Resultado de los patrones
    resultadoPatrones = [0,0,0,0]

    for i in range(len(listasPatrones)):
        # Longitud del patrón elegido
        patron_len = len(listasPatrones[i])
        for j in range(len(text) - patron_len + 1):
            # Comprueba si el patrón se encuentra en el texto cogiendo la longitud del patrón
            if text[j:j + patron_len] == listasPatrones[i]:
                resultadoPatrones[i] += 1
    
    # Muestra el resultado utilizando un método
    displayResult(text, resultadoPatrones)

# Muestra el resultado de los patrones
def displayResult(text, result):
    print(f"El texto \"{text}\" contiene los siguientes patrones:")
    print("00:", result[0])
    print("101:", result[1])
    print("ABC:", result[2])
    print("HO:", result[3], "\n")

if __name__ == '__main__':
    # Lista con pruebas para numeroPatrones
    pruebas = [
        "000",          # 00: 2
        "101",          # 101: 1
        "DABCABC",      # ABC: 2
        "HOHOHO",       # HO: 3
        "0010101",      # 00: 1, 101: 2
        "ABCHOHO",      # ABC: 1, HO: 2
        "00ABC101HO",   # 00: 1, 101: 1, ABC: 1, HO: 1
        "000101ABC",    # 00: 2, 101: 1, ABC: 1
        "HO10100ABC",   # 00: 1, 101: 1, ABC: 1, HO: 1
        "10100HOABC"    # 00: 1, 101: 1, ABC: 1, HO: 1
    ]

    for prueba in pruebas:
        numeroPatrones(prueba)