""""
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, 
de altura el número introducido.
"""

custom_input = int(input('Introduce un numero entero: '))

for i in range(0,custom_input):
    print("*"*(i+1))
