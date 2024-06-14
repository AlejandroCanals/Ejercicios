"""
Encontrar el número máximo en un array de números aleatorios
Descripción:
Desarrolla un programa en Python que genere un array de 10 números aleatorios enteros entre un
rango especificado (por ejemplo, entre 1 y 100). Y el programa debe de imprimir la lista de números
enteros, y después indicar cual es el número máximo del ejercicio e indicar su posición en el array.
Prohibido:
- Usar la función max()
Consejos:
- Puedes utilizar la función random.randint() para generar un número aleatorio dentro de un
rango específico.
Ejemplo de ejecución:
Array generado: [4, 2, 3, 6, 7, 5, 5, 10, 8, 10]
El número más alto de la lista es: 10 y está en la posición 7 del array"""

import random

numbers = []
for i in range(0, 10):
    numbers.append(random.randint(1, 10))

print(f'Array generada: {numbers}')

idx = 0
max = 0
idx_max = 0

for number in numbers:
    if(max < number):
        max = number
        idx_max = idx
    idx += 1
    print(idx)

print(numbers)
print(f'El numero mas alto de la lista es: {max} y está en la posición {idx_max} del array')