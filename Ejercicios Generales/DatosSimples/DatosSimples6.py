"""
Una panadería vende barras de pan a 3.49€ cada una. 
El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

numero de barras no diarias
precio habitual de la barra
descuento
coste final

"""

def precio_pan_de_ayer(cantidad):

    precio_barra_del_dia = 3.49
    print('El precio habitual es :', precio_barra_del_dia)
    descuento = 0.6
    pan_de_ayer = precio_barra_del_dia * descuento

    descuento_total = precio_barra_del_dia - pan_de_ayer
    print('Se va aplicar un descuento del 60% que corresponde a :',round(descuento_total,2))

    print('El coste final es de :' , round(pan_de_ayer,2))

precio_pan_de_ayer(1)