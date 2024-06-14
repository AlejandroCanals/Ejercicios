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

def devolverInt(str):
    valor = None
    while(valor is None):
        try:
            valor = int(input(str))
        except:
            print('El formato introducido no es correcto')
            print('Reintentando...')
    return valor

def introduceUnaLetra(str):
    valor = None
    while(valor is None):
        valor = input(str)
        if(len(valor) == 1):
            valor_is_int = True
            try:
                int(valor)
            except:
                valor_is_int = False
                
            if(valor not in ' .,()+-/@!¿?¡ºª' and valor_is_int is False):
                return valor
            else:
                print('El formato introducido no es correcto')
                print('Reintentando...')
        else:
            print('No puedes escribir mas de una letra')
        valor = None
    return valor

def mostrarPalabra(palabra, intentos):
    letras_usadas = []

    intentos_totales = intentos
    while(intentos > 0):
        letra = None
        print(f'Tienes {intentos} intentos restantes')
        while(letra is None):
            letra = introduceUnaLetra('Introduce una letra: ')
            if(letra in letras_usadas):
                print('Ya has escrito esta letra')
                letra = None
        letras_usadas.append(letra)

        palabra_mostrada = ''
        for i in range(0, len(palabra)):
            if palabra[i] in letras_usadas:
                palabra_mostrada += palabra[i]
            else:
                palabra_mostrada += '_'
            
        if(palabra == palabra_mostrada):
            print(f'¡Felicidades! Adivinaste la palabra: "{palabra}" en {intentos_totales - intentos} intentos.')
        else:
            print(f'Palabra: {palabra_mostrada}')
        intentos -= 1

palabras = ['periquito', 'comida', 'jamon', 'cocina', 'programacion', 'trabajador', 'examen', 'deportista']
palabra = palabras[random.randint(0, len(palabras) - 1)]

print(f'He pensado en una palabra de {len(palabra)} letras ¡Adivina cual es!')

intentos = devolverInt('Escribe la cantidad de intentos que quieres disponer: ')

mostrarPalabra(palabra, intentos)