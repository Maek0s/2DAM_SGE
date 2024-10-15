'''
Autor: Marcos Zahonero Martínez
Name of Problem: Convert string to camel case
Difficulty: 6 kyu
Categories: Regular Expressions, Algorithms, Strings
Statement: https://www.codewars.com/kata/517abf86da9663f1d2000003
'''
def to_camel_case(text):
    letter = ""
    txtConverted = ""
    lastChanged = 0
    for i in range(len(text)):
        if (text[i] == "-" or text[i] == "_"):
            letter = text[i + 1].upper()
            txtConverted += text[lastChanged: i] + letter
            lastChanged = i + 2
    txtConverted += text[lastChanged: len(text)]
    return txtConverted