'''
Autor: Marcos Zahonero Martínez
Name of Problem: Sum of Digits / Digital Root
Difficulty: 6 kyu
Categories: Mathematics, Algorithms
Statement: https://www.codewars.com/kata/541c8630095125aba6000c00
'''
def digital_root(n):
    txt = str(n)

    while (len(txt) > 1):
        suma = 0
        for letter in txt:
            suma += int(letter)
        txt = str(suma)
    return int(txt)