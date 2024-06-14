"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario
 donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario 
 si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura
   y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

    facturas = {
        'numero de factura' : 'valor coste'

    }

    Funcionalidades
        agregar nuevas facturars
            numero de factura
            coste
            agregar diccionario
        pagar una existente
            numero de factura
            eliminar del diccionario
        terminar
    Despues de cada operacion mostrar la cantidad cobrada y la de pendiente de cobro

"""
cantidad_cobrada = 0.0
pendiente_cobro = 0.0

facturas = {

}
pregunta = ''

print(facturas)


while pregunta.lower() != 'salir' :

    pregunta = input('Quieres comenzar agregar facturar o pagar existentes o salir? agregar/pagar/salir ')

    if pregunta.lower() == 'agregar':
        numero_factura = (input('Cual es el numero de la factura? '))
        coste_factura = float(input('Cual es el coste de la factura? '))
        facturas[numero_factura] = coste_factura
        pendiente_cobro += facturas[numero_factura]
        print('Tu factura se agrego correctamente',facturas)
        print('La cantidad pendiente de cobro es', pendiente_cobro)

        agregar_factura = input('Quieres agregar otra factura?') 
        while agregar_factura.lower() == 'si':
            numero_factura = (input('Cual es el numero de la factura? '))
            coste_factura = float(input('Cual es el coste de la factura? '))
            facturas[numero_factura] = coste_factura
            pendiente_cobro += facturas[numero_factura]
            
            print('Tu factura se agrego correctamente, tus facturas actuales son :',facturas)
            print('La cantidad pendiente de cobro es', pendiente_cobro)
            agregar_factura = input('Quieres agregar otra factura?') 



    elif pregunta.lower() == 'pagar':
            print('Tus facturas actuales son:', facturas)
            print('La cantidad pendiente de cobro es', pendiente_cobro)
            numero_factura = (input('Cual es el numero de la factura a pagar? '))
            if numero_factura in facturas:
                        cantidad_cobrada += facturas[numero_factura]
                        pendiente_cobro -= facturas[numero_factura]
                        print("Cantidad cobrada hasta ahora:", str(cantidad_cobrada))
                        print("Cantidad pendiente de cobro hasta ahora:", str(pendiente_cobro))
                        facturas.pop(numero_factura)
                        print('Tu factura se eliminó correctamente, tus facturas restantes son:', facturas)
                   
                        
         
    elif pregunta.lower() == 'salir':
         print('Has salido correctamente')
         break
         