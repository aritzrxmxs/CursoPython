print('*** Argumentos variables ***')

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - Nombre: {nombre} - {args}')
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar a la funcion
superheroe_superpoderes('Spiderman', 'Peter Parker', 'Instinto arácnido', 'Teleraña')
superheroe_superpoderes('Iron Man', 'Tony Stark', 'Armadura', 'Playboy', 'Millonario')

# Es opcional enviar argumentos variables

superheroe_superpoderes('Victoria', 'Acosta')