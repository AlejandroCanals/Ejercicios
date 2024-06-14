"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""


invertido= int(input('Cuanto quieres invertir : '))
interes_anual = int(input('Introuce tu interes anual : '))
anos = int(input('introuduce tus anos de inversion: '))

for i in range(anos):
    
    invertido *= 1 + interes_anual / 100

    print("Capital tras " + str(i+1) + " años: " + str(round(invertido, 2)))