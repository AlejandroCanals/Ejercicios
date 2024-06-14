"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. 
Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

fecha = input('Introduce la fecha en este formato dd/mm/aaaa: ')

primera_barra = fecha.find('/')
ultima_barra = fecha.rfind('/')

dia = fecha[:primera_barra]
mes = fecha[primera_barra+1:ultima_barra]
año = fecha[ultima_barra+1:]

print(dia + '\n' + mes + '\n' + año)
