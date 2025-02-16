import json
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# URL de la API Rest de Odoo
API_URL = 'http://localhost:8069/gestion/apirest/socio/'

# Función para crear un socio
def crear_socio(nombre, apellidos, num_socio):
    data = {'nombre': nombre, 'apellidos': apellidos, 'num_socio': num_socio}

    # Codificar los datos en formato JSON y luego en formato URL
    data_json = json.dumps(data)
    data_encoded = requests.utils.quote(data_json)  # Codificar el JSON para que se pueda usar en la URL

    # Construir la URL final con los datos
    url_final = f'{API_URL}?data={data_encoded}'

    print(f'URL que se va a enviar: {url_final}')  # Imprimir la URL para verificar

    try:
        response = requests.post(url_final)
        print(f'POST {API_URL} - Status Code: {response.status_code}, Response: {response.text}')

        if response.status_code == 200:
            return "Socio creado con éxito."
        else:
            return f"Error al crear el socio. {response.text}"
    except Exception as e:
        print(f"Error en crear_socio: {str(e)}")
        return "Error de conexión, servidor no disponible o no encontrado."

# Función para modificar un socio
def modificar_socio(nombre, apellidos, num_socio):
    data = {'nombre': nombre, 'apellidos': apellidos, 'num_socio': num_socio}
    try:
        # Generar la URL de modificación sin usar ID directamente en la URL
        url = f'{API_URL}?data={json.dumps(data)}'
        print(f'PUT {url} - Enviando datos para modificar socio.')
        response = requests.put(url, json={'data': data})  # Aquí enviamos los datos correctos
        print(f'PUT {url} - Status Code: {response.status_code}, Response: {response.text}')
        if response.status_code == 200:
            return "Socio modificado con éxito."
        else:
            return f"Error al modificar el socio. {response.text}"
    except Exception as e:
        print(f"Error en modificar_socio: {str(e)}")
        return "Error de conexión, servidor no disponible o no encontrado."

# Función para consultar un socio
def consultar_socio(num_socio):
    try:
        # Preparar el parámetro de la consulta
        data = {'num_socio': num_socio}
        url = f'{API_URL}?data={json.dumps(data)}'  # Codificar `data` para que sea parte de la URL
        response = requests.get(url)
        print(f'GET {url} - Status Code: {response.status_code}, Response: {response.text}')
        
        if response.status_code == 200:
            return f"Datos del socio: {response.json()}"
        else:
            return f"Socio no encontrado. {response.text}"
    except Exception as e:
        print(f"Error en consultar_socio: {str(e)}")
        return "Error de conexión, servidor no disponible o no encontrado."

# Función para borrar un socio
def borrar_socio(num_socio):
    data = {'num_socio': num_socio}
    try:
        # Enviar la solicitud DELETE con el parámetro `data` codificado en la URL
        url = f'{API_URL}?data={json.dumps(data)}'
        response = requests.delete(url)
        print(f'DELETE {url} - Status Code: {response.status_code}, Response: {response.text}')
        if response.status_code == 200:
            return "Socio borrado con éxito."
        else:
            return f"Error al borrar el socio. {response.text}"
    except Exception as e:
        print(f"Error en borrar_socio: {str(e)}")
        return "Error de conexión, servidor no disponible o no encontrado."

# Función para manejar los comandos del bot
async def handle_command(update: Update, context: CallbackContext):
    # El comando comienza con /start, por lo que debemos ignorar eso y procesar el resto
    command = update.message.text[len('/start '):].strip()  # Ignora '/start '
    
    # Dividir la acción (crear, modificar, etc.) del resto de parámetros
    parts = command.split(',')
    action = parts[0].strip().lower()  # Acción: crear, modificar, etc.
    
    if action == 'crear':
        # Obtener los parámetros del comando
        params = {key_value.split('=')[0].strip(): key_value.split('=')[1].strip() for key_value in parts[1:]}
        nombre = params.get('nombre')
        apellidos = params.get('apellidos')
        num_socio = params.get('num_socio')
        response = crear_socio(nombre, apellidos, num_socio)
    elif action == 'modificar':
        params = {key_value.split('=')[0].strip(): key_value.split('=')[1].strip() for key_value in parts[1:]}
        nombre = params.get('nombre')
        apellidos = params.get('apellidos')
        num_socio = params.get('num_socio')
        response = modificar_socio(nombre, apellidos, num_socio)
    elif action == 'consultar':
        num_socio = parts[1].split('=')[1].strip()
        response = consultar_socio(num_socio)
    elif action == 'borrar':
        num_socio = parts[1].split('=')[1].strip()
        response = borrar_socio(num_socio)
    else:
        response = "Orden no soportada. Usa 'crear', 'modificar', 'consultar' o 'borrar'."

    await update.message.reply_text(response)

# Función principal
def main():
    # Token del bot (coloca tu token aquí)
    TOKEN = "8033782672:AAGvU7Z0wbJblR8laIkxeC5zm6OqF05f8Ew"

    # Crear el bot
    application = Application.builder().token(TOKEN).build()

    # Agregar un manejador para el comando
    command_handler = CommandHandler('start', handle_command)
    application.add_handler(command_handler)

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()