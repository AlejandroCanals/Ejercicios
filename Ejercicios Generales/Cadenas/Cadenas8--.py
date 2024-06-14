"""
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y

 muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""

precio_producto = input('Cual es el precio? ')


print ((precio_producto[:precio_producto.find('.')]) ,'euros con ', (precio_producto[precio_producto.find('.')+1:]), 'centimos')