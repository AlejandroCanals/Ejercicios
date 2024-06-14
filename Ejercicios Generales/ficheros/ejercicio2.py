"""
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
done n es el número introducido, y la muestre por pantalla. 
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

def mostrar_fichero(n):
    nombre_fichero = 'table-' + str(n) + '.txt'
    try:
        f = open(nombre_fichero,'r')
    except FileNotFoundError:
        print('No se ha podido encontrar el fichero')

    else:
        print(f.read())
        f.close()

mostrar_fichero(5)