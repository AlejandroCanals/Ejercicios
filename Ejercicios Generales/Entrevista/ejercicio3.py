def programa():
    solictud = input('Introduce una cadena: ')
    solicitud2 = input('Introuce una letra a buscar: ')

    contador = 0
    cadena_convertida = ""
    for letra in solictud:
        if letra in solicitud2:
            cadena_convertida += letra.upper()
            contador += 1
        else:
            cadena_convertida += letra
    
    print(cadena_convertida)
    print(f"La letra {solicitud2} tiene {contador} letras")
   
            




(programa())