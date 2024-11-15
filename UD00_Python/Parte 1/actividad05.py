'''
Autor: Marcos Zahonero
Fecha: 16/10/2024
Descripción: Actividad 5, input de información y sobrecarga de funciones
'''

# Sobrecarga de funciones #
# En Python no funciona como se conoce la sobrecarga de funciones en Java
# ya que la última función reemplaza a la anterior, por lo que no se puede
# se puede hacer algo similar a sobrecargar pero seria con *args que todo
# lo que introduzcas en la función quedará guardado, mandes lo que le mandes:

def suma(*args):
    return sum(args)

# Input de información #
# Para introducir información se hace con input(), asignandolo ya a una variable
# en caso de que sea un int deberíamos castearlo ese input() para que sea un int

nombre = input("Introduce tu nombre: ")
num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))

seguir = input("Quieres poner otro número? (S/N): ").capitalize()

if (seguir == "S"):
    num3 = int(input("Introduce otro número: "))
    print(suma(num1, num2, num3))
else:
    print("Decidiste no poner otro número o no pusiste \"S\", suma de num1 y num2: ",end="")
    print(suma(num1, num2))

