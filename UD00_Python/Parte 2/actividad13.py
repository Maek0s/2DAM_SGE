'''
Autor: Marcos Zahonero
Fecha: 19/11/2024
Descripción: Actividad 13, utilizar una API desde Python de Rick and Morty.
Extra: He tenido que volcar toda la información a un archivo JSON ya que
sino te daba únicamente 20 personajes máximo, también he desplegado una lista
de las especies existentes en ese multiverso.
'''
import requests
import json

# Ejecuta este archivo desde la carpeta "Parte 2" sino habrá problemas con la ruta del archivo JSON

print("- = Lista de especies = -\n")
print("Human")
print("Animal")
print("Alien")
print("Humanoid")
print("Robot")
print("Cronenberg")
print("Mythological Creature")
print("Poopybutthole")

# Pedir al usuario la especie que quiere buscar
especie = input("\nIntroduce la especie que quieras pedir: ")

# Hacer la petición a la API
url = f"https://rickandmortyapi.com/api/character/?species={especie}"

# Contador para saber cuantos personajes se han encontrado
resultados = 0

# Lista para guardar todos los personajes
todos_los_personajes = []

# Mientras que haya una URL valida se ejecutará el bucle
# este se volverá "None" en cuanto no haya más páginas
while url:
    # Hacer la petición
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Añadir los personajes a la lista extendiendo la lista con data
        todos_los_personajes.extend(data["results"])

        # Si hay más páginas, se cambia la URL a la siguiente
        url = data["info"]["next"]
    else:
        # Si no se ha encontrado la especie o hay un error en la petición
        if (todos_los_personajes.isEmpty()):
            print("No se han encontrado personajes con esa especie o Error en la petición")
        break

# Guardar la respuesta en un archivo JSON
with open('actividad13Json/respuesta.json', 'w') as json_file:
    json.dump(todos_los_personajes, json_file, indent=4)

for personaje in todos_los_personajes:
    print(f"Nombre: {personaje["name"]}")
    print(f"Estado: {personaje["status"]}")
    print(f"Especie: {personaje["species"]}")
    print(f"Origen: {personaje["origin"]["name"]}")
    print(f"Episodios: {len(personaje["episode"])}")
    print("\n")

    resultados += 1

# Print con la cantidad de resultados encontrados y su especie.
print(f"Se han encontrado \033[1m{resultados}\033[0m personajes con la especie \033[1m{especie}\033[0m.")