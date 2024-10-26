'''
Autor: Marcos Zahonero Martínez
Name of Problem: Moving Zeros To The End
Difficulty: 5 kyu
Categories: Arrays, Sorting, Algorithm
Statement: https://www.codewars.com/kata/52597aa56021e91c93000cb0
'''
def move_zeros(lst):
    amountStart = lst.count(0)
    print(amountStart)
    amount = lst.count(0)
    while (amount != 0):
        lst.remove(0)
        amount = lst.count(0)

    for i in range(amountStart):
        lst.append(0)

    return lst