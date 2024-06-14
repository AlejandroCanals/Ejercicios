"""
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

"""


custom_input = "20,30,40,50"

ganadores = custom_input.split(',')

ganadores = [int(numero) for numero in ganadores]

ordenados = sorted(ganadores)

print(ordenados)