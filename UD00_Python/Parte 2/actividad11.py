'''
Autor: Marcos Zahonero
Fecha: 17/11/2024
Descripción: Actividad 11, interfaz gráfica con inicio de sesión con Kivy.
'''

from kivy.lang import Builder
from kivymd.app import MDApp
import csv

class MainApp(MDApp):

    # Diccionario para guardar las credenciales
    credenciales = {}

    # Método para construir la aplicación
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.loadCredentials()
        return Builder.load_file('actividad11/login.kv')

    # Método para cargar las credenciales
    def loadCredentials(self):
        with open("actividad11/users.csv") as File:
            reader = csv.reader(File, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for linea in reader:
                username, password = linea
                if username == "Usuario" and password == "Contraseña":
                    continue
                self.credenciales[username] = password
        print(self.credenciales)
        print("Credenciales cargadas")
                
    # Método para comprobar las credenciales
    def checkCredentials(self, username, password):
        if (username in self.credenciales):
            if (self.credenciales[username] == password):
                return True
        return False

    # Método para hacer login
    def login(self):
        username = self.root.ids.username.text
        password = self.root.ids.password.text

        if (self.root.ids.username.text != ""):
            self.root.ids.lblWelcome.text = f"¡Hola {self.root.ids.username.text}!"

            if self.root.ids.password.text != "":
                if self.checkCredentials(username, password):
                    self.root.ids.lblWelcome.text = f"¡Aceptado!"
                else:
                    self.root.ids.lblWelcome.text = f"¡Error!"

    # Método para limpiar los campos
    def clear(self):
        self.root.ids.username.text = ""
        self.root.ids.password.text = ""
        self.root.ids.lblWelcome.text = "¡Bienvenido!"

app = MainApp().run()