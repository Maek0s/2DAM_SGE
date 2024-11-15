'''
Autor: Marcos Zahonero
Fecha: 15/11/2024
Descripción: Actividad 7, funciones esPalindromo() y esPrimo() con doctest y archivos.
'''

def esPalindromo(number):
    """
    Devuelve True si el número es un palíndromo, False en caso contrario.

    >>> esPalindromo(121)
    True
    >>> esPalindromo(123)
    False
    >>> esPalindromo(11)
    True
    """

    return str(number) == str(number)[::-1]

def esPrimo(number):
    """
    Devuelve True si el número es primo, False en caso contrario.

    >>> esPrimo(2)
    True
    >>> esPrimo(4)
    False
    >>> esPrimo(7)
    True
    """

    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    import doctest

    palindromos = 0
    primos = 0
    dobles = []

    # IMPORTANTEE!! A LA HORA DE EJECUTAR DESDE EL TERMINAL DEBES ESTAR EN LA MISMA
    # CARPETA QUE EL ARCHIVO "exempleEntrada.txt" Y "exempleSalida.txt" SINO NO FUNCIONA

    # Abre el archivo y lee los números
    with open("actividad07Txts/exempleEntrada.txt", "r") as file:
        numeros = file.readlines()

    doctest.testfile("actividad07Txts/exempleEntrada.txt")

    for linea in numeros:
        numero = int(linea.strip())  # Convierte cada línea en un número
        resultadoPalindro = esPalindromo(numero)
        resultadoPrimo = esPrimo(numero)

        if resultadoPalindro:
            palindromos += 1
        if resultadoPrimo:
            primos += 1
        if resultadoPalindro and resultadoPrimo:
            dobles.append(numero)
        
    file.close()

    with open("actividad07Txts/exempleSalida.txt", "w") as file:
        file.write(f"Hay {palindromos} números palindromos.\n")
        file.write(f"Hay {primos} números primos.\n")
        for numero in dobles:
            file.write(f"{numero}\n")
    
        

