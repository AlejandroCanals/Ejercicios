"""
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
 Escribir otra función que reciba el diccionario generado con la función anterior y 
devuelva una tupla con la palabra más repetida y su frecuencia.
"""
def contar_palabras(cadena):
    cadena = cadena.split()
    palabras = {}

    for i in cadena:
        if i in palabras:
            palabras[i] += 1

        else:
            palabras[i] = 1

    return palabras

diccionario = contar_palabras('hola hola que tal estas estas hola')

print(diccionario)

def mas_repetida(diccionario):
    palabra_max= None
    minimo = 0

    for palabra,frecuencia in diccionario.items():
        if frecuencia > minimo:
            minimo = frecuencia
            palabra_max = palabra
    return palabra_max, minimo



print(mas_repetida(diccionario))

