#Ejercicio 5
#Construir un pequeño programa que convierta números binarios en enteros. 


numero_binario = input('Inserte un numero binari:')
numero_entero = int(numero_binario,2)
print(f"El numero entero es {numero_entero}")


"""Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""


año_curso =int(input('Ingresa año en curso: '))

# Para cada persona
for i in range(3):
    nombre = input("Ingrese su nombre:")
    nacimiento = int(input("Ingrese su año de nacimiento:"))

    edad = año_curso - nacimiento
    print (f"Cumplias {edad} años este curso")