'''
Autor: Marcos Zahonero Martínez
Name of Problem: Find the odd int
Difficulty: 6 kyu
Categories: Fundamentals
Statement: https://www.codewars.com/kata/54da5a58ea159efa38000836
'''
def find_it(seq):

    seq.sort()
    for elemento in seq:
        if (seq.count(elemento) % 2 != 0):
            return elemento

    return None