"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

"""
factura = float(100)


def calcular_iva(factura,iva=21):
    iva = iva/100
    porcenta_iva = factura * iva
    total = porcenta_iva + factura
    return total

print(calcular_iva(factura))