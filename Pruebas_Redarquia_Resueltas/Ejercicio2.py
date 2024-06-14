#EJERCICIO 1
"""
Calculadora de IMC
Descripción:
El índice de masa corporal (IMC) es una medida que se utiliza para calcular la cantidad de grasa
corporal de una persona. Se calcula dividiendo el peso de una persona en kilogramos por su altura
en metros al cuadrado.
Objetivo:
Escribir un programa en Python que calcule el IMC de una persona a partir de su peso y altura
introducidos por el usuario.
Requisitos:
- El programa debe solicitar al usuario que introduzca su peso en kilogramos.
- El programa debe solicitar al usuario que introduzca su altura en metros.
- El programa debe calcular el IMC utilizando la siguiente fórmula:
- El programa debe mostrar el IMC calculado al usuario.
- El programa debe mostrar un mensaje que interprete el valor del IMC según la siguiente
tabla:
IMC Interpretación
Menos de 18.5 Bajo peso
Entre 18.5 y 24.9 Peso normal
Entre 25 y 29.9 Sobrepeso
30 o más Obesidad
Consejos:
- Puedes utilizar la función float() para convertir las entradas del usuario de cadenas a
números.
- Puedes utilizar la función round() para redondear el valor del IMC a dos decimales.
- Puedes utilizar la función input() para pedir una entrada de valor al usuari"""
#TENEMOS 


def devolverFloat(str):
    valor = None
    while(valor is None):
        try:
            valor = float(input(str))
        except:
            print('El formato introducido no es correcto')
            print('Reintentando...')
    return valor

def defineMessage(imc):
    if(imc < 18.5):
        return 'Usted tiene un peso bajo'
    elif(18.5 <= imc and imc < 25):
        return 'Usted tiene un peso normal'
    elif(25 <= imc and imc < 30):
        return 'Usted tiene sobrepeso'
    elif(30 <= imc):
        return 'Usted tiene obesidad'
    else:
        return 'El valor devuelto no es válido'

peso = devolverFloat('Introduce tu peso: ')

altura = devolverFloat('Introduce tu altura: ')

imc = round(peso / (altura ** 2), 2)


print(f'Su IMC es {imc}')
print(defineMessage(imc))
