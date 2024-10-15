'''
Autor: Marcos Zahonero Martínez
Name of Problem: Simple Pig Latin
Difficulty: 5 kyu
Categories: Regular Expressions, Algorithms
Statement: https://www.codewars.com/kata/520b9d2ad5c005041100000f
'''
def pig_it(text):
    list = text.split(" ")
    texto = ""
    
    for i in range(len(list)):
        letter = list[i][0]
        if (list[i] != '?' and list[i] != '!'):
            list[i] = list[i][1:len(list[i])] + letter + "ay"
            texto += list[i] + " "
        else:
            texto += list[i] + " "
    return texto.strip()