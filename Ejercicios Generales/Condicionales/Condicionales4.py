"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

numero = int(input('Introuce un numero entero:'))

if numero % 2 == 0:
    print("tu numero " + str(numero) + " es par ")
else:
    print('No es par')