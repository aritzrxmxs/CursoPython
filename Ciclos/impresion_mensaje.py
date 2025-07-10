print('*** Repeticion de un mensaje ***')

mensaje = input('Introduce un mensaje: ')
numero_repeticiones = int(input('Cuantas veces quieres que se repita: '))

for _ in range(numero_repeticiones):
    print(mensaje, end = ' ')