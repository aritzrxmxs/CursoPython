print('*** Resivision numero positivo ***')

numero = int(input('Introduce un numero: '))

if numero > 0:
    print(f'El numero {numero} es positivo.')
elif numero < 0:
    print(f'El número {numero} es negativo.')
else:
    print(f'El numero {numero} es 0.')