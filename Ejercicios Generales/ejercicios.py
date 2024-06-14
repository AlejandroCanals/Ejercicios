#1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

def Max(num1,num2):
    
    if num1 >= num2 :
        return num1
    
    else:
        return num2

resultado = numMax(2,2)

#print(resultado)


#2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

def max_de_tres(num1,num2,num3):

    if num1 >= num2 and num1>= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#print(max_de_tres(8,7,6))

#1,2 con funcion max predeterminada

lista = [1,2,10,5,20]
maximo = max(lista)
#print (maximo)




#3 - Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def longitud(string):
    contador = 0
    for i in string:
        if i != ' ':
            contador += 1
        
    return contador

#print(longitud('hola que '))
#print (f"La longitud es {longitud_list1}")
#print (f"La longitud es {longitud_string}")


#4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.


def es_vocal(caracter):
    vocales = ['a','e','i','o','u']

    if caracter in vocales:
        return True
    else:
        return False
    

#print(es_vocal("e"))
#print(es_vocal("h"))

#5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
#  Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(list):
    total = 0
    for i in list:
        total += i
    return total

#print (sum([1,2,3,4]))


def multiplicar(list):
    total = 1
    for i in list:
        total *= i
    return total


    
#print  (multiplicar([1,2,3,4]))

#7 Fucnion que devuelva los caracteres de un texto 

def devolver_caracter(texto):
    caracteres = []

    for i in texto:
        caracteres.append(i)
    return caracteres

#print(devolver_caracter('hola que tal estais'))


#print (resultado3)


#6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"


def inversa(palabra):

    palabra_invertida = palabra[::-1]
    print(palabra_invertida)

#inversa('estoy probando')



# - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
#  ejemplo: es_palindromo ("radar") tendría que devolver True.


def palindromo(palabra):

    palabra_invertida = palabra[::-1]

    if palabra_invertida == palabra:
        return True
    else:
        return False
    
#print(palindromo('reconocer'))




#8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. 
# Escribir la función usando el bucle for anidado.

def superposicion(lista1,lista2):

    for i in lista1:
        for j in lista2:
            if i == j:
                return True
    else:
        return False

lista1 = ["Carol","Pepe"]
lista2 = ["Juan", "Jorge"]

print(superposicion(lista1,lista2))


#print (superposicion(lista1,lista2))