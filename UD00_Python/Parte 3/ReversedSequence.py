'''
Autor: Marcos Zahonero Martínez
Name of Problem: Reversed sequence
Difficulty: 8 kyu
Categories: Fundamentals
Statement: https://www.codewars.com/kata/5a00e05cc374cb34d100000d
'''
def reverse_seq(n):
    list = []
    for i in range(n,0,-1):
        list.append(i)
    return list