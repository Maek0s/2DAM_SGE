'''
Autor: Marcos Zahonero Martínez
Name of Problem: Get the Middle Character
Difficulty: 7 kyu
Categories: Fundamentals, Strings
Statement: https://www.codewars.com/kata/56747fd5cb988479af000028
'''
def get_middle(s):
    middle = int(len(s) / 2)
    
    if (len(s) <= 2):
        return s
    else:
        if (len(s) % 2 == 0):
            return s[middle - 1] + s[middle]
        elif (len(s) % 2 != 0):
            return s[middle]