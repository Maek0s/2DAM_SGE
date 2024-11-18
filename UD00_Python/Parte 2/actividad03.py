'''
Autor: Marcos Zahonero
Fecha: 18/11/2024
Descripción: Actividad 3, identificar el número de patrones.
'''

def numeroPatrones(text):
    listasPatrones = []

    ptr00 = 0 # Patrón 00
    ptr101 = 0 # Patrón 101
    ptrABC = 0 # Patrón ABC
    ptrHO = 0 # Patrón HO

    # puedo hacer un for con todos los patrones y que checkee la iteracion para sumar
    # checkear tambien si tiene siguiente caracter y arreglar cuando son 2 caracteres en vez de 3
    for i in range(len(text)):
        print()

    return listasPatrones

if __name__ == '__main__':
    # Tests #

    numeroPatrones("000")