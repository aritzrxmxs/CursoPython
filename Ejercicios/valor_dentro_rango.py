VALOR_MINIMO = 0
VALOR_MAXIMO = 5

print('*** Validador de rango ***')

numero = int(input(f'Introduce un numero entre {VALOR_MINIMO} y {VALOR_MAXIMO}: '))

esta_rango = VALOR_MINIMO <= numero <= VALOR_MAXIMO

print(f'Esta el número \'{numero}\' dentro del rango? : {esta_rango} ')