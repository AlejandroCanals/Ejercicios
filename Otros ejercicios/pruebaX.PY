

# Un dia extra es agregado cada 4 anos que es el 29 de febrero y ese dia se llama leap_day 
# Un leap_year contiene un leap_day

# En el calendario gregoriano se usan estas condiciones para saber si es un ano bisiestos 
    # el ano se puedo divivr por 4 a no ser que
        #tambien sea divisible entre 100 NO ES BISIESTO , A NOSER QUE 
            #tambien sea divisble entre 400 entonces si es bisiestos


def is_int(str):
    valor = None
    while valor is None:
        try:
            valor = int(input(str))
        except ValueError:
            print('Introduce un numero entero')
            print('Reintentando...')
    return valor



def is_leap(year):
    leap = False
    
    # Write your logic here
   
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = False
    return leap



year = is_int('Introduce un numero: ')

is_leap(year)