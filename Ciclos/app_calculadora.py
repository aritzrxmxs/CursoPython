end = False

while not end:
    print('''--- CALCULADORA ---
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    opcion = int(input('Selecciona una opción: '))
    if 1 <= opcion <= 4:
        num1 = float(input('Número 1: '))
        num2 = float(input('Número 2: '))
    if opcion == 1:
        print(f'El resultado de la suma es: {num1 + num2}')
    elif opcion == 2:
        print(f'El resultado de la resta es: {num1 - num2}')
    elif opcion == 3:
        print(f'El resultado de la multiplicación es: {num1 * num2}')
    elif opcion == 4:
        print(f'El resultado de la división es: {num1 / num2:.2f}')
    elif opcion == 5:
        print('Saliendo de la calculadora.')
        end = True
    else:
        print('Introduce una opción válida.')
