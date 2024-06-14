"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""




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

def caculo():
    print('Introduce un primer numero entero')
    n = int(input())
    print('Introduce un segundo numero entero')
    m = int(input())

    c = n / m
    r = n % m

    return c , r

print('Tu cociciente es :',caculo(c))