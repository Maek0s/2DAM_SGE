'''
Autor: Marcos Zahonero Martínez
Name of Problem: Descending Order
Difficulty: 7 kyu
Categories: Fundamentals
Statement: https://www.codewars.com/kata/5467e4d82edf8bbf40000155
'''
def descending_order(num):
    list = []
    result = ""
    
    for i in range(len(str(num))):
        list.append(str(num)[i])

    list.sort()
    list.reverse()
    
    for element in list:
        result += element
    
    return int(result)