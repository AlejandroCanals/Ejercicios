
"""
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def custom_max(n1:int,n2:int):

    if n1 >= n2:
        return n1
    else:
        return n2


print (custom_max(190,210))


"""
2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def max_de_tres(n1,n2,n3):

    if n1 >= n2 and n1 >=n3:
        return n1
    elif n2 >= n1 and n2>= n3:
        return n2
    else:
        return n3
    

print (max_de_tres(10,10,11))


"""
 Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() incorporada, 
 pero escribirla por nosotros mismos resulta un muy buen ejercicio.


"""

strings = ['hola','vale','cocodrilo']

def longitud_lista(string):
    contador = 0
    
    for caracter in string:
        contador +=1
    
    return contador

print(longitud_lista(strings))


"""
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""

vocales = ['a','e','i','o','u']

def es_vocal(caracter):

    for vocal in vocales:
        if vocal == caracter:
            return True
    
    else:
        return False

    
print (es_vocal('u'))

"""
5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
 Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.


"""

numeros = [1,2,3,4]

def sum(lista:int):

    total = 0
    for numero in lista:
        total = total + numero
    
    return total

print (sum(numeros))
        

def multip(lista):

    total = 1
    
    for numero in lista:
        total  *= numero

    return total

print(multip(numeros))


"""
 6.Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse" MIRAR
 def inversa (cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1
    return invertida
"""
cadena = "estoy probando"

def inversa(cadena):
    cadena_invertida = cadena[::-1]
    return cadena_invertida

print(inversa(cadena))
        
"""
 Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
   ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(cadena):

    invertida = cadena[::-1]

    if cadena == invertida:
        return True
    else:
        return False
    
print(es_palindromo('pelota'))


"""

Definir una función superposicion() que tome dos listas y
 devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
    
 Resultado = (Compra1,Compra2) = True
 Resultado = (Compra1, Compra3) = False
 Resultado = (Compra2, Compra3) = True


"""
compra1 = ['platano','tomate','lechuga']

compra2 = ['platano','lechuga','mandarina']

compra3 = ['pera','manzana','mandarina']

def superposicion(lista1,lista2):

    for fruta1 in lista1:
        for fruta2 in lista2:
            if fruta1 == fruta2:
                return True
    else:
        return False

print(superposicion(compra1,compra3))

"""
9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

"""


def generar_n_caracteres(n:int,string):
    
    multiplicacion = n * string 
    return multiplicacion

print(generar_n_caracteres(10,"x"))
    

"""
10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******

"""

enteros = [4,5,6]

def histograma(lista):
    dibujo = "*"
    total = ''
    for numero in lista:
       total += numero * dibujo + "\n"
    
    return total

print (histograma(enteros))