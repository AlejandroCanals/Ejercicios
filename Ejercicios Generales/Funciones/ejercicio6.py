"""
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
Suma: 2 + 3 + 4 + 5 + 6 = 20
Divide: 20 ÷ 5 = 4
"""


lista = [2,3,4,5,6]



def calcular_media(lista):
    suma = 0
    for numero in lista:
        suma += numero
    
    media = suma / len(lista)

    return media
  

calcular_media(lista)