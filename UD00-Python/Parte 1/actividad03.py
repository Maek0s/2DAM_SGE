'''
Autor: Marcos Zahonero
Fecha: 14/10/2024
Descripción: Actividad 3, cifrado de contraseñas
'''

import hashlib

# Guía: https://recursospython.com/guias-y-manuales/hashlib-md5-sha/

# Función que cifra una contraseña
def cifrarContraseña(password):
    h = hashlib.sha256(password.encode())

    return h.hexdigest()

# Registrar usuario con la contraseña en una lista
def registrarUsuarioEnLista(username, password):
    # Le pongo un "|" para separar el username y la contraseña cifrada
    # para en caso de hacer un split dividirlo fácilmente.
    credentialsList.append(username + "|" + cifrarContraseña(password))
        
# Registrar usuario con la contraseña en un diccionario
def registrarUsuarioEnDict(username, password):
    # Para veririficar si existe otro usuario con ese nombre
        if (credentialsDict.get(username) == None):
            credentialsDict[username] = cifrarContraseña(password)
        else:
            print("El usuario ya existe.")

# Ejemplos de uso en Lista

credentialsList = []

registrarUsuarioEnLista("marcos", "1234")
registrarUsuarioEnLista("paco", "paco123")
registrarUsuarioEnLista("oscar", "garcia")
registrarUsuarioEnLista("username", "password")
registrarUsuarioEnLista("antonio", "431223")

for user in credentialsList:
    print(user)

print("\n")

# Ejemplo de uso en Diccionario

credentialsDict = {}

registrarUsuarioEnDict("marcos", "1234")
registrarUsuarioEnDict("paco", "paco123")
registrarUsuarioEnDict("oscar", "garcia")
registrarUsuarioEnDict("username", "password")
registrarUsuarioEnDict("antonio", "431223")

# Registro un usuario que ya existe para comprobar que no deja
registrarUsuarioEnDict("marcos", "1234")

# Bucle para recorrer el Diccionario de forma ordenada
for clave, valor in credentialsDict.items():
    print(f"User - {clave} = {valor}")