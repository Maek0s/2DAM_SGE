'''
Autor: Marcos Zahonero
Fecha: 14/10/2024
Descripción: Actividad 4, explicación de operadores 'is', 'not' y in' en Py3
'''

# Operador 'is' #
# Este operador (is) podemos utilizarlo para comprobar si 2 variables son una copia del otro

# Vemos aquí una lista y luego directamente una copia exacta, sin volcar sus datos, directamente una copia.
lista1 = [5, 1218, 231]
lista1_copia = lista1
lista2 = [5, 1218, 231]

print(lista1 is lista1_copia) # Nos devuelve "True" porque son la misma lista
print(lista2 is lista1) # Nos devuelve "False" porque son listas diferentes, a pesar de que tengan los mismos valores

print("\n= = = = \n")

# Operador 'not' #
# Este operador (not) se utiliza para negar una condición, por ejemplo, si la condición da "True", con esto devuelve "False"

# Veamos un ejemplo aquí, de algo muy simple de ver
verdadero = True
falso = False

print(not verdadero) # Nos devuelve "False" porque la condición es "True", y estamos negando la condición con "not" al inicio
print(not falso) # Nos devuelve "True" porque la condición es "False"

print("\n= = = = \n")

# Operador 'in' #
# Guía detallada: https://realpython.com/python-in-operator/
# Este operador (in) se utiliza para comprobar si un valor está en una lista, tupla, diccionario, y más.

# Un ejemplo de lista, veamos si el siguiente número está en la lista
listaNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(5 in listaNums) # Nos devuelve "True" porque el número 5 está en la lista
print(11 in listaNums) # Nos devuelve "False" porque el número 11 no está en la lista

print()

# Un ejemplo en una cadena, veamos si la siguiente palabra/letra está en la cadena
cadena = "Hola me llamo Marcos Zahonero"

print("Marcos" in cadena) # Nos devuelve "True" porque "Marcos" está en la cadena
print("Óscar" in cadena) # Nos devuelve "False" porque no se encuentra en la cadena
print("a" in cadena) # Nos devuelve "True" porque la letra "a" está en la cadena

print("\n= = = = \n")

# Dato extra del 'not' junto al 'in' #
# Podemos utilizar el 'not' junto al 'in' para comprobar si un valor NO está en una lista, tupla, ...

numerosLoteria = [231, 4324, 12312, 544124, 21312]

if 123 not in numerosLoteria:
    print("El número no está en la lista.")
if 231 in numerosLoteria:
    print("El número está en la lista.")