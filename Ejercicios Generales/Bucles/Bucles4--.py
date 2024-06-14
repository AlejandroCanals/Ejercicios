"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta
cero separados por comas.
"""

custom_input = int(input('Escribe un numero entero positivo: '))

for i in range(custom_input,0,-1):
    print(i, end=', ')