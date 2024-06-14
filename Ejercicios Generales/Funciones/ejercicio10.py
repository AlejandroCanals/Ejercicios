"""
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

11100 = 


"""

def decimal_a_binario(numero):
    if numero == 0:
        return '0'
    binario = ''
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return binario

# Ejemplo
numero_decimal = 13
print("El número decimal", numero_decimal, "en binario es:", decimal_a_binario(numero_decimal))

def binario_a_decimal(binario):
    decimal = 0
    potencia = 0
    for bit in binario[::-1]:
        decimal += int(bit) * (2 ** potencia)
        potencia += 1
    return decimal

# Ejemplo
numero_binario = '1101'
print("El número binario", numero_binario, "en decimal es:", binario_a_decimal(numero_binario))
