'''
Autor: Marcos Zahonero
Fecha: 15/11/2024
Descripción: Actividad 1, explicación y ejemplo de funciones en Python (map(), filter() y reduce()).
'''

# Colores para la terminal
negrita = "\033[1m"
reset = "\033[0m"

## Explicación de una función lambda en Python ##

#  Una función lambda en Python es una función anónima, es decir, una función que no tiene nombre.
#  Se utiliza para crear funciones pequeñas y simples de manera rápida.
# La sintaxis básica de una función lambda es:

# lambda argumentos: expresión

suma = lambda a, b: a + b
print(suma(5, 8)) # Salida: 13

## Ejemplo con map(), filter() y reduce() ##

 # map() aplica una función a todos los elementos de una lista
 # La función map() toma dos argumentos: una función y una lista.

print(f"{negrita}Función map() {reset}\n",end="\n")

entrada = input("Introduce una cadena de números separados por espacios: ")
numeros = list(map(int, entrada.split())) # Convierte la cadena de números en una lista de números enteros
print("Lista de números enteros:", numeros)


# filter(), como su nombre indica filtra los elementos, en este caso se usa en una lista

print(f"\n{negrita}Función filter() {reset}\n",end="\n")

numeros_menor10 = list(filter(lambda x: x < 10, numeros))
print("Números < 10:", numeros_menor10)


# reduce() aplica una función a los elementos de una lista de manera acumulativa

print(f"\n{negrita}Función reduce() {reset}\n",end="\n")

from functools import reduce # Importamos la función reduce de la librería functools sino no funciona

mult_total = reduce(lambda x, y: x * y, numeros) # Multiplica todos los elementos de la lista
print("Multiplicación total:", mult_total)