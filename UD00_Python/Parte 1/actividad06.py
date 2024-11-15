'''
Autor: Marcos Zahonero
Fecha: 18/10/2024
Descripción: Actividad 6, ordenamiento de listas con sorted() y key function.
'''

# Lista con varias listas con los valores: [altura, peso]
lista = [
    [180, 75],
    [165, 70],
    [180, 65],
    [190, 80],
    [165, 80],
    [190, 70]
]

# Función clave (key function)
# Esta función se utiliza para decidir cómo ordenar los elementos de la lista
# Parecido al compareTo de java cuando implementamos la interfaz Comparable<T>.
# Primero ordenamos por altura en orden descendente
# y, en caso de igualdad en la altura, ordenamos por el peso en orden ascendente (x[1]).
def key_function(x):
    return (-x[0], x[1])

# Usamos sorted() con la key_function para ordenar la lista.
lista_ordenada = sorted(lista, key=key_function)

# Imprimimos la lista ordenada
print(lista_ordenada)