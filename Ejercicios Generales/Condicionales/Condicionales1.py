#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def mayor_edad():
    edad = int(input('Cual es tu edad:'))

    if edad >= 18:
        print('ERES MAYOR DE EDAD')
    
    else:
        print('ERES MENOR DE EDAD')


