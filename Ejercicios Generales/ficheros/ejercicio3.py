"""
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, 
y muestre por pantalla la línea m del fichero. 
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

def dos_numeros(n1,n2):

    nombre_fichero = 'table-' + str(n1) + '.txt'

    try:
        f = open(nombre_fichero,'r')
        linea = f.readlines()
        print(linea[n2-1])

    except FileNotFoundError:
        print('No se ha podido encontrar el arhcivo')

dos_numeros(5,6)