'''
Autor: Marcos Zahonero
Fecha: 14/10/2024
Descripción: Actividad 2, funcionamiento de métodos
'''

import copy

def suma(a, b):
    return a + b

def modificarLista(list):
    for i in range(len(list)):
        list[i] *= 2

def copiarModificarLista(lista):
    lista_copy = copy.deepcopy(lista)
    for i in range(len(lista_copy)):
        lista_copy[i] *= 2

    return lista_copy

# Defino el main para que se ejecute el código
if __name__ == "__main__":
    # Ejemplo de suma
    num1 = 3
    num2 = 5
    print(f"La suma de {num1} y {num2} es: {suma(num1, num2)}")

    # Ejemplo del método modificarLista
    list_original = [1, 2, 3, 4]
    modificarLista(list_original)
    print(f"Lista modificada: {list_original}")

    # Ejemplo del método copiarModificarLista
    list_original = [1, 2, 3, 4]
    list_modificada = copiarModificarLista(list_original)
    print(f"Original: {list_original}")
    print(f"Modificada: {list_modificada}")