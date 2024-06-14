"""
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. 
Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

lista = [1,2,5,8,10]

def max_in_list(lista):
    mayor = lista[0]

    for numero in lista:
        if numero > mayor:
            mayor = numero
    return mayor

#max_in_list(lista)


"""
Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

palabras = ['hola','perfecto','tranquilo','sssssssssssssssssssssssss']

def mas_larga(lista):

    respuesta = lista[0]

    for palabra in lista:
        if len(palabra) > len(respuesta):
            respuesta = palabra
    
    return respuesta

#mas_larga(palabras)


"""
Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
"""

lista3= ['hola','perfecto','bien']


def filtar_palabras(lista,n):

    palabras_filtradas = []
    for palabra in lista3:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)
    return palabras_filtradas

#(filtar_palabras(lista3,1))

"""
Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

    input()
    
"""

def programa():
    solicitud  = input('Introduce una cadena: ')
    contador = 0

    for letra in solicitud :
        if letra.isupper():
            contador +=1
    print(f'Esta cadena tiene {contador} en mayusculas')

#programa()

"""
Ejercicio 5
Construir un pequeño programa que convierta números binarios en enteros.
"""

def binario_a_entero(binario):

    entero = int(binario,2)

    return entero

    

#print(binario_a_entero("1010"))

"""
Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""



def calcular_edad():
    año_en_curso = int(input('Introuce el año actual:'))
    personas = []
    for i in range(3):
        nombre = str(input('Intruce tu nombre:'))
        año_nacimiento = int(input('Introuce tu año de nacimiento:'))
        edad = año_en_curso - año_nacimiento
        personas.append({'nombre':nombre, 'año_nacimiento':año_nacimiento, 'edad':edad})

    for persona in personas:
        print(f"{persona['nombre']} va a cumplir {persona['edad']}")

#calcular_edad()


"""
Ejercicio 7
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

edades = (30,40,20,50,10,60,54,6,2,3)

mayores_de_veinte= []
for edad in edades:
    if edad > 20:
        mayores_de_veinte.append(edad)

#print(mayores_de_veinte)


"""Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)"""

nombres = ['Alejandro','Belen','Armando','Gonzalo']

def letra_en_lista(lista):
    letra_a_buscar= str(input('Introduce una letra para la busqueda: '))
    resultado = []
    for nombre in nombres:
        if nombre[0] == letra_a_buscar:
            resultado.append(nombre)
            
    return resultado

#print(letra_en_lista(nombres))

"""
Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas 
las vocales.
Se puede hacer que el usuario sea quien elija la palabra.

"""

def contar_vocales(cadena):
    
    vocales = 'aeiou'
    cadena = cadena.lower()

    for vocal in vocales:
        contador = 0
        for letra in cadena:
            if vocal == letra:
                contador += 1
    
        print(f"Hay {contador} {vocal}")

contar_vocales('hoooooola')


"""
Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""
def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def calculadora(m,n):
    total= 1

    for i in range(n):
        total *= m

    return total


def conteo_palabra(frase):
    palabras = frase.split(" ")
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1  
    return conteo

#print(conteo_palabra('hola hola que tal estas'))

numeros_desordenados = [8,5,3,6,0,1,3]

def custom_sorted(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1] , lista[j]
    
    return lista

numeros_ordenados = custom_sorted(numeros_desordenados)

#print (numeros_ordenados)


def contar_vocales(palabra):
    vocales = ["a","e","i","o","u"]
    contador_vocales = {vocal:0 for vocal in vocales}

    for letra in palabra:
        if letra.lower() in vocales:
            contador_vocales[letra.lower()] += 1

    return contador_vocales

print(contar_vocales('holaaaaaei'))