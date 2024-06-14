"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

"""

password = input('Guarda contraseña: ')
pregunta = input('Introduce tu contrasena: ')

while pregunta != password:
    print('Contraseña incorrecta, prueba otra')
    pregunta = input('Introduce tu contrasena: ')
else:
    print('Contraseña correcta')