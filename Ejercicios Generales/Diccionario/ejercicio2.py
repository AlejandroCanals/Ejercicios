"""
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
 Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""




base_datos = []

def crear_datos():
    nombre = input('Intruduce nombre: ') 
    edad = input('Intruduce edad: ') 
    direccion = input('Intruduce direccion: ') 
    movil = input('Intruduce movil: ') 

    datos_usuario = {
        'nombre':nombre,
        'edad': edad,
        'direccion': direccion,
        'movil': movil
    }

    base_datos.append(datos_usuario)


crear_datos()
crear_datos()


print(base_datos)
