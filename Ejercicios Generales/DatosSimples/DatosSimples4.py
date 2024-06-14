"""
Ejercicio 10

Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
 Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos
y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.


*Cobro por peso
*Payasos = 112g
*Mueñecas = 75g
"""



def calcular_peso(payasos,muñecas):

    coste_payasos = payasos * 112
    coste_muñecas = muñecas * 75

    total = coste_payasos + coste_muñecas

    return total

print('Cuantos payasos tienes:')
payasos_vendidos = int(input())

print('Cuantos munecas tienes:')
muñecas_vendidas = int(input())


total_peso = calcular_peso(payasos_vendidos,muñecas_vendidas)

print("El peso es total es ", total_peso)

