"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""


eco = input()

while eco:
    print(eco)
    eco = input()
    if eco == 'salir':
        print('Has salido del bucle jeje')
        break
        