# Hacer un piedra papel o tijera
import random


def piedra_papel_tijera():
    ganador_usuario = 0
    ganador_ordenador = 0

    while ganador_usuario < 3 and ganador_ordenador < 3:

        usuario = input('Elige piedra , papel o tijera: ')
        opciones = ['piedra', 'papel', 'tijera']
        ordenador = random.choice(opciones)
        print(f'Usuario elige : {usuario} y ordenador elige: {ordenador}')

        if usuario not in opciones:
            print('No has introducido una opcion valida')

        else:
            if usuario == ordenador:
                print('Empataste')

            elif (usuario == 'piedra' and ordenador == 'tijera') or \
                    (usuario == 'tijera' and ordenador == 'papel') or \
                    (usuario == 'papel' and ordenador == 'piedra'):
                ganador_usuario += 1
                print('Ganador de la ronda: Usuario')
            else:
                print('Ganador de la ronda: Ordenador')
                ganador_ordenador += 1
        print(
            f'Usuario tiene {ganador_usuario} puntos y el ordenador tiene {ganador_ordenador} puntos')

    if ganador_ordenador == 3:
        print('El ganador es ORDENADOR')
    elif ganador_usuario == 3:
        print('El ganador es USUARIO')


piedra_papel_tijera()
