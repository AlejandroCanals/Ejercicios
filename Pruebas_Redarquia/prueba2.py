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
- Puedes utilizar la función input() para pedir una entrada de valor al usuari
"""


def is_float(prompt: str) -> float:
  
    while True:
        try:
            valor = float(input((prompt)))
            return valor
        except:
            print('Has introducido un valor incorrecto. Por favor, intenta nuevamente.')


peso = is_float('Introduce tu peso: ')
altura = is_float('Introduce tu altura: ')
imc = round(peso / (altura ** 2),2)

def estado_imc(imc):

    if imc < 18.5:
        return 'Bajo peso'
    elif 18.5 < imc < 24.9:
        return 'Normal'
    elif 25 < imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

print(imc)
print(estado_imc(imc))