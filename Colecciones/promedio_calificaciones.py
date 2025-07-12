print('*** Promedio de Calificaciones ***')
numero_calificaciones = int(input('Introduce el no. de calificaciones: '))
calificaciones = []

for indice in range(numero_calificaciones):
    calificacion = int(input(f'Calificacion[{indice+1}] = '))
    calificaciones.append(calificacion)

print(f'Las calificaciones proporcionadas son: {calificaciones}')

suma = sum(calificaciones)
promedio = suma / numero_calificaciones

print(f'El promedio de las calificaciones: {promedio:.1f}')