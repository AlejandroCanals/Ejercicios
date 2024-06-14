"""
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando 
por la última.
"""

custom_word = input('Escribe una palabra: ')

for i in range(len(custom_word)-1,-1,-1):
    print (custom_word[i])