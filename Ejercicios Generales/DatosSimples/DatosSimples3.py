"""
Ejercicio 8

Escribir un programa que pida al usuario dos números enteros y 
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
 y <c> y <r> son el cociente y el resto de la división entera respectivamente.

 
n = input usuario
m = input  usuario

c = n / m
r = n % m

"""

def calculo():
    print('Introduce un primer numero entero')
    n = int(input())
    print('Introduce un segundo numero entero')
    m = int(input())

    c = n / m
    r = n % m

    return c , r

resultado_cociente , resultado_resto = calculo()

print('Tu cociciente es :',resultado_cociente, 'Tu resto es : ', resultado_resto)