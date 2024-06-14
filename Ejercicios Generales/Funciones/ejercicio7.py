"""
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
"""

lista = [2,5,10,]

def calcualar_cuadrado(lista):
    cuadrados = []

    for numero in lista:
        cuadrado = numero * numero
        cuadrados.append(cuadrado)

    print(cuadrados)

calcualar_cuadrado(lista)