"""

Ejercicio 4)
Juego de Adivinanzas con palabras
Descripción:
Desarrollar un programa en Python que implemente un juego de adivinanzas con palabras. El
programa debe seleccionar una palabra aleatoria de un diccionario y luego pedirle al jugador que
adivine la palabra letra por letra. El jugador tiene un número limitado de intentos para adivinar la
palabra correctamente.
Objetivo:
Practicar el uso de cadenas de texto, bucles y condiciones en Python.
Requisitos:
- El programa debe guardar como variable el siguiente diccionario de palabras:
palabras = ['periquito', 'comida', 'jamon', 'cocina',
'programacion', 'trabajador', 'examen', 'deportista']
- El programa debe seleccionar una palabra aleatoria del diccionario.
- El programa debe mostrar la palabra al jugador con las letras ocultas por guiones bajos (_).
- El programa debe solicitar al jugador que ingrese una letra.
- El programa debe verificar si la letra ingresada está en la palabra oculta.
- Si la letra está en la palabra, el programa debe mostrar la palabra actualizada con la letra
revelada.
- Si la letra no está en la palabra, el programa debe disminuir el número de intentos
restantes.
- El juego termina cuando el jugador adivina la palabra correctamente o cuando se agotan
los intentos.
- El programa debe mostrar un mensaje de felicitación o derrota al final del jue
"""
import random
import time
palabras = ['periquito', 'comida', 'jamon', 'cocina',
            'programacion', 'trabajador', 'examen', 'deportista']

palabra = random.choice(palabras)


def ingresar_letra():
    while True:
        letra = input('Introduce una letra: ')
        if len(letra) == 1:
            if letra.isalpha() is True:
                return letra
            else:
                print('No has introducido una letra')
        else:
            print('Has introducio mas de una letra, prueba otra')


def juego(palabra):
    letras_ingresadas = []
    intentos = 6
    print('-----EL JUEGO VA A COMENZAR------')
    while intentos > 0:
        letra = ingresar_letra()

        if letra in letras_ingresadas:
            print('Yas has introducido esa letra prueba otra')
        else:
            letras_ingresadas.append(letra)
            if letra not in palabra:
                intentos -= 1
                print(f'Te quedan {intentos} intentos')
                if intentos == 0:
                    print('--------Has perdido lo siento----------')
                    print(f'La palabra era {palabra}')
                    time.sleep(1)
                    break

        palabra_oculta = ''

        # Si la letra esta en la palabra , agrega la letra , sino agrega un _
        for i in range(0, len(palabra)):
            if palabra[i] in letras_ingresadas:
                palabra_oculta += palabra[i]
            else:
                palabra_oculta += '_'
        # Si la palabra es igual a la palabra oculta el jugador gana el juego
        if (palabra == palabra_oculta):
            print(
                f'------¡Felicidades! Adivinaste la palabra: "{palabra}" en {intentos} intentos.--------')
            time.sleep(1)
            break

        else:
            print(f'Palabra: {palabra_oculta}')

    #Reset del juego
    reset = input('---------Quieres volver a jugar?-------------\n')
    if reset.lower() == 'si':
        time.sleep(1)
        juego(random.choice(palabras))

    else:
        print('-----Okey gracias por jugar----------')


(juego(palabra))
