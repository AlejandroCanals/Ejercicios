""""
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
done n es el número introducido.
"""



def agregar_numero(n):
    
    nombre_fichero = 'table-' + str(n) + '.txt'
    f = open(nombre_fichero,'w')
    for i in range(1,11):
        f.write(str(n) + 'x' + str(i) + '=' + str(n* i) + '\n')
    
    f.close()

agregar_numero(5)