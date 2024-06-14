"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con 
los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por
pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.






"""
def menu():
    es_vegetariano = input('¿Eres vegetariano? (si/no): ')
    respuesta = es_vegetariano.lower()

    ingredientes_vegetarianos = ['pimiento', 'tofu']
    ingredientes_no_vegetarianos = ['peperoni', 'jamon', 'salmon']
    ingredientes_comunes = ['tomate', 'mozzarella']

    if respuesta == 'si':
        print('Nuestro menú es vegatariano es :', ingredientes_vegetarianos)
        eleccion = input('Elige un ingrediente: ')
      
        ingredientes_elegidos = [eleccion]
        ingredientes_elegidos.extend(ingredientes_comunes)
        
        print('Tu pizza lleva los siguientes ingredientes:', ingredientes_elegidos)
        print('La pizza elegida es vegetariana.')

    elif respuesta == 'no':
        print('Nuestro menú es:', ingredientes_no_vegetarianos)
        eleccion = input('Elige un ingrediente: ')

        ingredientes_elegidos = [eleccion]
        ingredientes_elegidos.extend(ingredientes_comunes)
        print('Tu pizza lleva los siguientes ingredientes:', ingredientes_elegidos)
        print('La pizza elegida no es vegetariana.')
    else:
        print('Respuesta inválida. Por favor, responde si o no.')

menu()
