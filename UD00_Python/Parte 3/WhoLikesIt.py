'''
Autor: Marcos Zahonero Martínez
Name of Problem: Who likes it?
Difficulty: 6 kyu
Categories: Strings, Fundamentals
Statement: https://www.codewars.com/kata/5266876b8f4bf2da9b000362
'''
def likes(names):
    txt = ""
    
    if (len(names) == 0):
        txt = "no one likes this"
    elif (len(names) == 1):
        txt = names[0] + " likes this"
    elif (len(names) == 2):
        txt = names[0] + " and " + names[1] + " like this"
    elif (len(names) == 3):
        txt = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif (len(names) >= 4):
        txt = names[0] + ", " + names[1] + " and " + str((len(names) - 2)) + " others like this"
    
    return txt