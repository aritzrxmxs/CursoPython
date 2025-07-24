print('*** Calculadora con Funciones ***')

def mostrar_menu():
    print('''Operaciones que puedes realizar:
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Salir''')
    return int(input('Escoge una opción: '))

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def pedir_numeros():
    numero1 = float(input('Introduce el número 1: '))
    numero2 = float(input('Introduce el número 2: '))
    return numero1, numero2

while True:
    mostrar_menu()
    opcion= mostrar_menu()

    if opcion == 1:
        a, b = pedir_numeros()
        print(f'El resultado de la suma es: {suma(a,b)}\n')
    elif opcion == 2:
        a, b = pedir_numeros()
        print(f'El resultado de la resta es: {resta(a,b)}\n')
    elif opcion == 3:
        a, b = pedir_numeros()
        print(f'El resultado de la multiplicación es: {multiplicacion(a,b)}\n')
    elif opcion == 4:
        a, b = pedir_numeros()
        print(f'El resultado de la división es: {division(a,b)}\n')
    elif opcion == 5:
        print('\nSaliendo del programa.. ¡Hasta pronto!')
        break
    else:
        print('Escoge una opción válida.')