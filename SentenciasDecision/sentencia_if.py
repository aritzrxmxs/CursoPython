print('*** Sentencia IF ***')

edad = int(input('Introduce tu edad: '))

if edad >= 18:
    print(f'Eres mayor de edad. Tienes {edad} años.')
elif 13 <= edad <=18:
    print('Eres un adolescente.')
else:
    print(f'Eres un niño. Tienes {edad} años.')
