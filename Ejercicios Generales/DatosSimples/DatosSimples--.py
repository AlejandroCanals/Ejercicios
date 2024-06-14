# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

#print('Hola mundo')

"""
Ejercicio 2

Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.
"""

Saludo = 'Hola mundo!'

#print(Saludo)

"""
Ejercicio 3

Escribir un programa que pregunte el nombre del usuario en la consola y
 después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
"""

#print('Cual es tu nombre?')
nombre = input()
#print (f'Hola {nombre}')

"""
Ejercicio 4

Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética
"""

#print(((3+2) / (2*5))**2)

"""
Ejercicio 5

Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde.

"""

horas_trabajadas = int(input('Introduce tus horas trabajadas en numero entero: '))
coste_hora = float(input('Cuanto cobras la hora: '))
total = horas_trabajadas * coste_hora

print(total)











def pregunta_horas_trabajas():
    while True:
        print('Cuantas horas trabajas')
        try:
            horas_trabajadas = int(input())
            break
        except ValueError:
            print('Debes ingresar un numero entero')
        

    while True:
        print('Cuanto cobras la hora?')
        try:
            coste_hora = float(input())
            break
        except ValueError:
            print('Debes ingresar un numero')

    cobro = horas_trabajadas * coste_hora

    return f'Te corresponde {cobro} euros la hora'

        

#print(pregunta_horas_trabajas())    
