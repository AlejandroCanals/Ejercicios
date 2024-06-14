#1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def numMax (num1,num2):

    if num1 > num2:
        return num1
    
    else:
        return num2
    

resultado = numMax(10,5)

print (resultado)

#2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def maxTres (num1,num2,num3):

    if num1 >= num2 and num1 >= num3 :
        return num1
    
    elif num2>= num1 and num2>= num3:
        return num2
    
    else:
        return num3
    

resultado2 = maxTres(2,6,5)

print(resultado2)

#1,2 con funcion max predeterminada

lista = [1,2,6,4,5]
mayor = max(lista)

print(mayor)


#3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def leng(iterable):
    longitud = 0

    for i in iterable:
        longitud += 1

    return longitud

string = 'Hola mundo2323' 
contador = leng(string)

print(contador)

#4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def contiene_vocal(caracter):
    if caracter == "a" or caracter == "e" or caracter == "i" or  caracter == "u":
        return True
    else:
        return False

    

vocabulario = contiene_vocal("a")

print(vocabulario)

#4 - Escribir una función que tome una palabra y devuelva True si es una vocal, de lo contrario devuelve False.

def vocal(caracter):
    vocales = ['a','e','i','o','u']
    return caracter in vocales

print(vocal('a'))

def palabra_vocal(palabra):
    for letra in palabra:
        if vocal(letra):
            return True
    
    return False

print(palabra_vocal('csss'))


#5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
#  Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(*args):
    total = 0
    for numero in args:
        total += numero

    return total

print(sum(1,2,3));

def multip(*args):
    total = 1 
    for numero in args:
        total *= numero

    return total

print(multip(1,2,3,4))

#7 Fucnion que devuelva los caracteres de un texto 

def text_caracter(palabra):
    caracteres= []
    for caracter in palabra:
        caracteres.append(caracter)
    return caracteres 
    
print(text_caracter('1234'))

#6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
def inversa(cadena):
    cadena_invertida = cadena[::-1]

    return cadena_invertida

texto = "estoy probando"
resultado = inversa(texto)
print (resultado)


# - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
#  ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

print(es_palindromo('radar'))

#8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
# Escribir la función usando el bucle for anidado.

lista1 = ['Tomate','Pechuga']
lista2 = ['tomate','Pollo']

def superposicion(lista1,lista2):
 
    for alimento1 in lista1:
        alimento1 = alimento1.lower()
        for alimento2 in lista2:
            alimento2= alimento2.lower()
            if alimento1 == alimento2:
                return True
    return False

print (superposicion(lista1,lista2))

#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. 
#Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande


def max_in_list(lista):
    maximo = lista[0]
    minimo = lista[0]

    for numero in lista:
        if numero > maximo:
            maximo = numero
        if numero < minimo:
            minimo = numero

    return maximo , minimo


my_list = [2,6,4,5]

print(max_in_list(my_list))


#Ejercicio 2
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 
  
def mas_largas(lista3):

    mas_larga = lista3[0]

    for palabra in lista3:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra
    return mas_larga

varios = ['caca','culo','loslideres']

print(mas_largas(varios))


#Ejercicio 2
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 

def mas_mas_larga(lista3):
    la_mas_larga= lista3[0]
    for palabra in lista3:
       if len(palabra) > len(la_mas_larga):
        la_mas_larga = palabra
    return la_mas_larga

print (mas_mas_larga(varios))


#Ejercicio 5
#Construir un pequeño programa que convierta números binarios en enteros. 

numero_binario = "1000111"

numero_entero = int(numero_binario)

print (numero_entero)