'''
Autor: Marcos Zahonero Martínez
Name of Problem: Create Phone Number
Difficulty: 6 kyu
Categories: Arrays, Strings, Regular expressions, Algorithms
Statement: https://www.codewars.com/kata/525f50e3b73515a6db000b83
'''
def create_phone_number(n):
    txt = "("
    
    for i in range(3):
        txt += str(n[i])
    
    txt += ") "
    
    for i in range(3):
        txt += str(n[i + 3])
        
    txt += "-"
    
    for i in range(4):
        txt += str(n[i + 6])
    
    return txt