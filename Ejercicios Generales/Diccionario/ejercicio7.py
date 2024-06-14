"""
Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste


"""
cesta_compra = {

}

trigger = input('Quieres empezar la compra: Si/No: ')

while trigger.title() == 'Si':

    articulo = input('Introduce nombre articulo')
    precio = float(input('Introuce precio: '))
    cesta_compra[articulo] = precio
    
    trigger = input('Quieres seguir comprando: Si/No')


precio_total = 0

for articulo, precio in cesta_compra.items():
    precio_total += precio

print('Lista de la compra: ' ,cesta_compra)

print ('El precio total de la cesta es :', precio_total)


"""
cesta_compra = {}

trigger = input('Quieres empezar la compra: Si/No: ')

while trigger.title() == 'Si':
    articulo = input('Introduce nombre del artículo: ')
    precio = float(input('Introduce precio del artículo: '))
    cesta_compra[articulo] = precio
    trigger = input('Quieres seguir comprando: Si/No ')

print("Lista de la compra:")
total = 0
for i, (articulo, precio) in enumerate(cesta_compra.items(), 1):
    print(f"Artículo {i}: {articulo}\tPrecio: {precio}")
    total += precio

print(f"Total\tCoste: {total}")
"""
