""" 
Escribe una funciona que acepte un string como argumneto
La funcion deberia poner en mayusuculas cada dos letras en la string
La funcion deberia retornar un string convertida
"""

"""
Hola = HoLa
Callate = CaLlAtE

Pepito = PepIto

"""

def cada_dos_letras_mayusculas(string):
    resultado = ""

    for i in range(len(string)):
        if i % 2 == 1 and string[i] != ' ':
            resultado += string[i].upper()
        else:
            resultado += string[i]
    return resultado

print(cada_dos_letras_mayusculas('hola'))



def cada_tres_letras_mayusculas(string):
    resultado2= ""
    contador = 0

    for char in string:
        if contador == 3 :
            resultado2 += char.upper()
            contador = 0
        else:
            resultado2 += char.lower()
        
        if char != ' ':
            contador += 1

    return resultado2
    

#print(cada_tres_letras_mayusculas('Pepito los santos'))
        

        
def cada_cuatro_letras_mayuscualas(string):
    resultado3 = ""
    contador = 0
    primer_caracter_palabra = True

    for char in string:
        
        if contador == 4:
            resultado3 += char.upper()
            contador = 0
        elif primer_caracter_palabra:
            resultado3 += char.upper()
            primer_caracter_palabra = False
        
        else:
            resultado3 += char.lower()
        
        if char == ' ':
            primer_caracter_palabra = True
        else:
            contador += 1
    return resultado3

#print(cada_cuatro_letras_mayuscualas("abcdefghi pepe"))

"""
a 0
b 1
c 2
d 3
E 4
f 0
g 1
h 2
i 3
"""

def primera_letra_mayuscula(string):

    primera_letra_mayuscula= True
    resultado4= ""
    
    for char in string:
        if primera_letra_mayuscula:
            resultado4 += char.upper()
            primera_letra_mayuscula = False
        else:
            resultado4 += char.lower()

        if char == ' ':
            primera_letra_mayuscula = True

    return resultado4

#print(primera_letra_mayuscula('opiace sdoasda sdasdsa'))

def cada_cinco_letras_mayuscula(string):
    contador = 0
    resultado5 = ""
    first_letter_word = True

    for char in string:
        if contador == 6:
            resultado5 += char.upper()
            contador = 0

        elif first_letter_word :
            resultado5 += char.upper()
            first_letter_word = False        
            contador = 0
        else :
            resultado5 += char.lower()
        
        if char == " ":
            first_letter_word = True
        
        else :
            contador += 1

    return resultado5

#print(cada_cinco_letras_mayuscula('sdsdsddsds sds ddqweqeq sadsad qeqwe ssds'))