"""
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
 
"""

def descuento(price,discount):
   
   return price - price * discount / 100


def iva(price,percentage):
    
    return price + price * percentage / 100



"""
Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y
   una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y 
   devolver el precio final de la cesta.
"""


def calcular_compra(cesta,function):

    total = 0
    for price, discount in cesta.items():
        total += function(price, discount)
    return total


print('El precio de la compra tras aplicar los descuentos es: ', calcular_compra({1000:20, 500:10, 100:1}, descuento))
print('El precio de la compra tras aplicar el IVA es: ', calcular_compra({1000:20, 500:10, 100:1}, iva))