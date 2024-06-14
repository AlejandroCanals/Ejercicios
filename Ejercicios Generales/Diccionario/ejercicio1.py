"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
 muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""


monedas =  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}


divisa = input('Elige un divisa euro ,dollar , yen')



for nombre,simbolo in monedas.items():

    if divisa.capitalize() == nombre:
        print(simbolo)

