'''
Autor: Marcos Zahonero Martínez
Name of Problem: Highest and Lowest
Difficulty: 7 kyu
Categories: Fundamentals, Strings
Statement: https://www.codewars.com/kata/554b4ac871d6813a03000035
'''
def high_and_low(numbers):
    import numpy as np # type: ignore

    list = numbers.split(" ")
    listNums = np.array(list, dtype=int)

    listNums.sort()
    resultado = str(listNums[len(listNums) - 1]) + " " + str(listNums[0])
    return resultado