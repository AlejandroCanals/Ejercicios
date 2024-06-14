""""
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
"""

numeros = [2,3,5,6,7]

str_numeros = ','.join(map(str,numeros))
print(str_numeros)



def calcular_media(lista):
 
    suma_total = 0

    for numero in numeros:
        suma_total += numero

    media = suma_total / len(numeros)
    diccionario= {}

    
    diccionario[str_numeros] = media

    return diccionario 

print(calcular_media(numeros))