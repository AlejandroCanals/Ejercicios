"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y
 muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales,
el número de unidades con tres dígitos y 
 el coste total con 8 dígitos enteros y 2 decimales.
"""

producto = input('Nombre del producto: ')
precio = float(input('Precio del producto: '))
unidades = int(input('Número de unidades: '))

# Formatear el precio unitario con 6 dígitos enteros y 2 decimales
precio_unitario_formateado = '{:,.2f}'.format(precio)

# Formatear el número de unidades con tres dígitos
unidades_formateadas = '{:03d}'.format(unidades)

# Calcular el coste total
coste_total = unidades * precio

# Formatear el coste total con 8 dígitos enteros y 2 decimales
coste_total_formateado = '{:,.2f}'.format(coste_total)

# Imprimir el resultado
print(f'{producto}: {precio_unitario_formateado} € unidad x {unidades_formateadas} unidades = {coste_total_formateado} €')
