"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta 
ese número separados por comas.

"""


def numero_entero():
    while True:
        valor = input('Introduce un numero entero: ')

        try:
            valor = int(valor)
            return valor
        except ValueError:
            print('No has introducido un numero entero valido')
       
def mostrar_impares(numero):
    for i in range(1,(numero)+1,3):
        print(i,end=',')



numero = numero_entero()
mostrar_impares(numero)