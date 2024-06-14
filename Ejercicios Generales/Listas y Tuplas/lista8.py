"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

palabra = input('Escribe una palabra: ')

palabra = list(palabra)

print(palabra)

reverse_palabra = list(palabra)
reverse_palabra.reverse() 

print(reverse_palabra)

if palabra == reverse_palabra:
    print('Es palindromo')
else:
    print('No es palindromo')