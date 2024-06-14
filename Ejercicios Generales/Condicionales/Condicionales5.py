"""
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y 
sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

"""

def tributas(edad,ingresos):
    
    if (ingresos) >= 1000 and edad >= 16 :
        print ('te toca pagar')
    else:
        print('No tienes que tributar ')


tributas(18,15000)
