#Ejercicio 1
#La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), solo van a funcionar para 2 o 3 números. 
#Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.

my_list = [2,3,4,10,22,1]


def max_in_list(list):
    maximo = list[0]
    minimo = list[0]

    for numero in my_list:
        if numero >= maximo:
            maximo = numero
        if numero <= minimo:
            minimo = numero
    
    print(maximo,minimo)

max_in_list(my_list)



#Otros ejemplos mios

def multiplicar_in_list(lista):
    total = 1
    for numero in lista:
        total *= numero
    
    print(total)

#multiplicar_in_list(my_list)



def dividir(lista):
    resultado = lista[0]
    for numero in lista[1:]:
        resultado /= numero 
    return resultado

#print(dividir([10,5]))

#Ejercicio 2
#Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga. 

list_palabras = ['pedro','paconi','sulftao','capitalista']

def mas_larga(lista):
   
    palabra_mas_larga = lista[0]

    for palabra in lista:
        if len(palabra) >= len(palabra_mas_larga):
            palabra_mas_larga = palabra

    return palabra_mas_larga


#print(mas_larga(list_palabras))


#ejercicios inventado por mi
#De la la lista de palabra devuelve cuanto caracteres tiene cada palabra

def conteo_caracteres(lista):
    conteo = []

    for palabra in lista:
        conteo.append(len(palabra))
    
    return conteo

#print(conteo_caracteres(list_palabras))


#Ejercicio 3
#Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres. 

def filtar_palabrar(lista,n):
    filtro = []
    for palabra in lista:
        if len(palabra) > n:
            filtro.append(palabra)

    return filtro

#print(filtar_palabrar(list_palabras,2))


#Ejercicio 4
#Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene. 

def programa():
    
    custom_input = input('Ingresa una cadena: ')
    contador = 0
    for i in custom_input:
        if i.isupper():
            contador += 1
    print(f'La cadena tiene {contador} mayusculas')
    return (contador)

programa()


#print(f"La cadena tiene {mayusuculas} letras mayusculas")

#Ejercicio 5
#Construir un pequeño programa que convierta números binarios en enteros. 


numero_binario = "1000111"

numero_entero = int(numero_binario)

#print (numero_entero)