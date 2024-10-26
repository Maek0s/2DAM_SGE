'''
Autor: Marcos Zahonero Martínez
Name of Problem: Bit Counting
Difficulty: 6 kyu
Categories: Bits, Algorithms
Statement: https://www.codewars.com/kata/526571aae218b8ee490006f4
'''
def count_bits(n):
    cont = 0
    while (n >= 1):
        if (n % 2 == 1):
            cont += 1
        n = int(n / 2)

    print(cont)
    return cont