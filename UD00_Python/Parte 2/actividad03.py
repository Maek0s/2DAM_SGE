'''
Autor: Marcos Zahonero
Fecha: 18/11/2024
Descripción: Actividad 3, identificar el número de patrones.
'''

def numeroPatrones(text):
    listasPatrones = ["00","101","ABC","HO"]
    resultadoPatrones = [0,0,0,0]

    ptr00 = 0 # Patrón 00
    ptr101 = 0 # Patrón 101
    ptrABC = 0 # Patrón ABC
    ptrHO = 0 # Patrón HO

    # puedo hacer un for con todos los patrones y que checkee la iteracion para sumar
    # checkear tambien si tiene siguiente caracter y arreglar cuando son 2 caracteres en vez de 3
    for i in range(len(listasPatrones)):
        for j in range(len(text)):
            if (text[j:len(text)] in listasPatrones[i]):
                resultadoPatrones[i] += 1
                print(text[j:len(text)], i, listasPatrones[i])
                
    return resultadoPatrones



if __name__ == '__main__':
    # Tests #

    print(numeroPatrones("000")) # 00: 2
    #numeroPatrones("101") # 101: 1
    #numeroPatrones("DABCABC") # ABC: 2
    #numeroPatrones("HOHOHO") # HO: 3