'''
Autor: Marcos Zahonero Martínez
Name of Problem: Split Strings
Difficulty: 6 kyu
Categories: Regular, Expressions, Algorithms
Statement: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001
'''
def solution(s):
    list = []
    
    while (len(s) != 0):
        if (len(s) == 0):
            break
        elif (len(s) == 1):
            s = s + "_"
        else:
            list.append(s[0:2])
            s = s[2:len(s)]
    return list