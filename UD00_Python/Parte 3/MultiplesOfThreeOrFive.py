'''
Autor: Marcos Zahonero Martínez
Name of Problem: Multiples of 3 or 5
Difficulty: 6 kyu
Categories: Mathematics, Algorithms
Statement: https://www.codewars.com/kata/514b92a657cdc65150000006
'''
def solution(number):
    sum = 0
    
    if number < 4:
        return 0
    
    for i in range(number - 1, 2, -1):
        if (i % 3 == 0):
            sum += i
        elif (i % 5 == 0):
            sum += i
    return sum