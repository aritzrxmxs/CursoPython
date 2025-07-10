print('*** Sistema de Administración de cuentas ***')
salir = False

while not salir:
    print(f'''Menu:
    1. Crear cuenta.
    2. Eliminar cuenta.
    3. Salir del programa.
''')
    opcion = int(input('Elige una opción: '))
    if opcion == 1:
        print('Creando cuenta \n')
    elif opcion == 2:
        print('Eliminando cuenta.. \n')
    elif opcion == 3:
        print('Saliendo del programa.. \n')
        salir = True
    else:
        print('\nIntroduce una opción correcta.')