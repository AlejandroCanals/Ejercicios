"""
Ejercicio 3)
Juego de Adivinanzas
Descripción:
Escribir un programa en Python que implemente un juego de adivinanzas clásico. El programa debe
pensar en un número aleatorio entre un rango especificado por el usuario y luego pedirle al usuario
que adivine el número. El programa debe dar pistas al usuario si su suposición es demasiado alta o
baja hasta que el usuario adivine correctamente el número.
Objetivo:
Practicar el uso de bucles, condiciones e interacción con el usuario en Python.
Requisitos:
- El programa debe solicitar al usuario que introduzca un límite inferior para el rango de
números aleatorios.
- El programa debe solicitar al usuario que introduzca un límite superior para el rango de
números aleatorios.
- El programa debe generar un número aleatorio dentro del rango especificado.
- El programa debe solicitar al usuario que introduzca una suposición.
- El programa debe comparar la suposición del usuario con el número aleatorio:
- Si la suposición es demasiado alta, el programa debe mostrar un mensaje que indique que
el usuario debe adivinar un número más bajo.
- Si la suposición es demasiado baja, el programa debe mostrar un mensaje que indique
que el usuario debe adivinar un número más alto.
- Si la suposición es correcta, el programa debe mostrar un mensaje de felicitación al
usuario y finalizar.
- El programa debe repetir el proceso de solicitar suposiciones y dar pistas hasta que el
usuario adivine correctamente el número.
Consejo:
- Puedes utilizar la función random.randint() para generar un número aleatorio dentro de un
rango específico
"""

import random


def is_int(prompt: str) -> int:
  
    while True:
        try:
            valor = int(input((prompt)))
            return valor
        except:
            print('Has introducido un valor incorrecto. Por favor, intenta nuevamente.')

upper_limit = is_int('Introduce un numero para establecer un rango maximo: ')
lower_limit = is_int('Introduce un numero para establecer un rango minimo: ')

aleatorio = random.randint(lower_limit,upper_limit)


def juego(aleatorio):
    print('EL JUEGO VA A COMENZAR!')
    print('-------------------------------------------------------')

    while True:
        suposicion = is_int('Introduce el numero que crees ')
        if suposicion == aleatorio:
            return('Has acertado el numero era {}'.format(aleatorio))
             
        elif suposicion > aleatorio:
            print('Tu suposicion es demasiado alta ,prueba con otra')
        elif suposicion < aleatorio:
            print ('Tu supocion es demasiado baja , prueba otra ')
        print('-------------------')
print(juego(aleatorio))