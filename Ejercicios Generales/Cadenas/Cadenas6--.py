"""
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla
 la misma frase pero con la vocal introducida en mayúscula.
"""

frase = input('introduce frase:')
vocal = input('Introduce vocal:')

vocal_mayus = vocal.upper()

print(frase.replace(vocal,vocal_mayus))