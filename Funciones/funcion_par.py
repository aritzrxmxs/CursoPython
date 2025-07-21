print('*** Funcion par ***')

def es_par(numero):
    if numero % 2 == 0:
        return 'Si'
    else:
        return 'No'

# Llamamos a la funcion
if __name__ == '__main__':
    numero = int(input('Dime un numero: '))
    print(f'El numero es par?: {es_par(numero)}')