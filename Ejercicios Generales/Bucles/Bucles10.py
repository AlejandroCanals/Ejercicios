"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
# Un numero primo es divisible por el mismo y entre 1 
"""
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2


while n % i != 0:
    i+=1
if i == n:
    print('es primico')
else:
    print('no es primico')