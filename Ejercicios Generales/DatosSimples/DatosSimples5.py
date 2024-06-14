"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año,
se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. 
Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

"""
"""
def cuenta_ahorra():
    print('Introduce la cantidad:')
    deposito = int(input())
    
    primer_año = deposito * 0.04 + deposito
    segundo_año = primer_año * 0.04 + primer_año
    tercer_año =  segundo_año * 0.04 + segundo_año

    print("Primer año:", primer_año)
    print("Segundo año:", segundo_año)
    print("Tercer año:", tercer_año)

cuenta_ahorra()
"""

def calcular_ahorro(tasa_de_interes,años):
    print('Cuanto saldo quieres introducir:')
    deposito = int(input())
    saldo = deposito
    for i in range(años):
        saldo += saldo * tasa_de_interes
    return saldo

tasa_de_interes = 0.04

saldo_primer_año=calcular_ahorro(tasa_de_interes,2)

print('el primer año :',saldo_primer_año)
    
