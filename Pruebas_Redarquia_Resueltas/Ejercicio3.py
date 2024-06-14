import random

def devolverInt(str):
    valor = None
    while(valor is None):
        try:
            valor = int(input(str))
        except:
            print('El formato introducido no es correcto')
            print('Reintentando...')
    return valor

def Juego(number):
    print('He pensado en un numero!')
    aleat = None
    while(aleat != number):
        aleat = devolverInt('Adivina cual es: ')
        if(aleat == number):
            print(f'¡Felicidades! Has adivinado el número correctamente. ¡Era el {number}!')
        elif(aleat < number):
            print('¡Tu suposición es demasiado baja! Intenta con un número más alto.')
        else:
            print('¡Tu suposición es demasiado alta! Intenta con un número más bajo.')

print('Bienvenido al juego de las adivinanzas!')
min = devolverInt('Introduzca un minimo para el rango del numero aleatorio: ')
max = devolverInt('Introduzca un maximo para el rango del numero aleatorio: ')

Juego(random.randint(min, max))
