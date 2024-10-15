'''
Autor: Marcos Zahonero
Fecha: 14/10/2024
Descripción: Actividad 1, diferencias entre shallow copy y deep copy y utilización de listas
'''

import copy

# ● Clonar una llista
list = [1, 2, 3, 4, 5]

# Shallow copy
shallowCopy = list.copy()

# Deep copy
deepCopy = copy.deepcopy(list)

# - El método para copiar de Shallow copy hace que cree una nueva lista, pero los valores
# de la lista son básicamente un acceso directo a los valores de la lista original, es decir,
# si cambias algo en el shallowCopy cambiaría en la lista original

# - Deep copy en cambio, crea una nueva lista que copia los valores pero no los enlaza,
# por lo que si cambias algo en la deepCopy no cambiará en la lista original

# ● Afegir un element a una llista
list.append(6)

# ● Llevar un element a una llista
list.remove(3)

# ● Crear una nova llista amb els 4 últims elements d’una llista
last4 = list[-4:]

# ● Convertir les paraules d’una cadena (separades per espai) a una llista
txt = "Hola me llamo Marcos Zahonero"
palabras = txt.split()

# ● Comentaris amb una línia
# Això és un comentari d'una línia

# ● Comentaris multilínia
"""
Això és un comentari
multilínia que pot
ocupar diverses línies
"""