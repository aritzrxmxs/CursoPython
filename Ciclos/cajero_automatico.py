cuenta_banco = 1000
salir = False
operacion = '¡Operación realizada con éxito!'
while not salir:
    print(f'''
----- MENU CAJERO -----
    1. Depositar dinero.
    2. Retirar dinero.
    3. Consultar saldo.
    4. Salir''')
    opcion = int(input('Selecciona una opción: '))

    if opcion == 1:
        depositar = float(input('Introduce la cantidad a depositar: '))
        cuenta_banco += depositar
        print(operacion)
    elif opcion == 2:
        retirar = float(input('Introduce la cantidad a retirar: '))
        if retirar > cuenta_banco:
            print(f'No tienes saldo suficiente. Saldo actual {cuenta_banco}€')
        else:
            cuenta_banco -= retirar
            print(operacion)
    elif opcion == 3:
        print(f'Su saldo actual es: {cuenta_banco:.2f}€')
    elif opcion == 4:
        print('Saliendo del programa. ¡Hasta pronto!')
        salir = True
    else:
        print('Elige una opción válida.')
