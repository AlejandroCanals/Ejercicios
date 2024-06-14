"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
 pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
 Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

"""

asignaturas = ['Mates','Historia','Fisica']
asignaturas_a_repitir = []


for i in asignaturas:
    evaluacion = input(f'Que has sacado en {i}')

    if int(evaluacion) < 5:
        asignaturas_a_repitir.append(i)
    
print('Tienes que repetir',asignaturas_a_repitir)