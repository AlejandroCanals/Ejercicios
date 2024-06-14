"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
"""

numero1 = int(input('Introduce un primer número: '))
numero2 = int(input('Introduce un segundo número: '))

if numero2 != 0:
    division = numero1 / numero2
    print("La división es:", division)
else:
    print("Error: No se puede dividir por cero.")
