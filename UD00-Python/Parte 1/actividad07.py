import random

class Car:
    def __init__(self, matricula, color):
        self.matricula = matricula;
        self.color = color;

    def imprimir(self):
        print("Matricula: ", self.matricula, ", color: " + self.color)

    def acelerar(self):
        print("Acelerando, matricula: ", self.matricula)

    def frenar(self):
        print("Frenando, matricula ", self.matricula)

    def generarColor():
        colors = ["Red", "White", "Black", "Pink", "Blue"]

        return colors[random.randint(0, len(colors) - 1)]

n = int(input("Introduce cuantos coches quieres crear: "))

listaCoches = []

# Generamos los coches y los guardamos
for i in range(1,n + 1):
    coche = Car(matricula=i, color=Car.generarColor())
    listaCoches.append(coche)

# Imprimimos los coches y hacemos que aceleren y frenen
for coche in listaCoches:
    coche.imprimir()
    coche.acelerar()
    coche.frenar()
    print()