from random import randint

print('*** Sistema generador de ID Unico ***')
nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido: ')
anio = input('Introduce tu año de nacimiento: ')

numero_aleatorio = randint(0000, 9999)

print(f'Hola {nombre},\n\tTu nuevo número de identificación (ID) generado por el sistema es:\n'
      f'\t{nombre[0:2].upper()}{apellido[0:2].upper()}{anio[2:]}{numero_aleatorio}\n'
      f'\tFelicidades!')