print('Bienvenidos a la casa de los espejos')

edad_cliente = int(input('Que edad tienes? '))
miedo_oscuridad = input('Tienes miedo a la oscuridad? (Si/No): ')
tienes_miedo = miedo_oscuridad.strip().lower() == 'si'

if edad_cliente >= 10 and not tienes_miedo:
    print('Puedes entrar.')
else:
    print('No puedes entrar.')