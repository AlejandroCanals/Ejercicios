"""
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
"""

def calcular_mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_mcm(a, b):
    return a * b // calcular_mcd(a, b)

# Ejemplo
num1 = 24
num2 = 36
print("El MCD de", num1, "y", num2, "es:", calcular_mcd(num1, num2))
print("El mcm de", num1, "y", num2, "es:", calcular_mcm(num1, num2))