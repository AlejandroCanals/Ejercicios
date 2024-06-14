"""
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
 Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde.

A = Mujer <m , Hombre > n
B =  resto

"""

genero  = input('Introuce tu genero: (M o H)')
name = input('Introuce tu nombre:')


if genero == "M" :
    if name.lower() < "m":
        group = "A"
    
    else:
        group = "B"

if genero == "H":
    if name.lower() > "n":
        group = "A"
    else:
        group ='B'

print('Tu grupo es :', group)