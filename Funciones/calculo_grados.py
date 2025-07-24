def grados_fahren(grados):
    return (grados * 1.8) + 32

def fahren_grados(fahren):
    return (fahren - 32) / 1.8
def pedir_datos():
    return float(input('Introduce el número a calcular: '))
while True:
    print('''
*** Menu ***
    1. De Grados a Fahrenheit
    2. De Fahrenheit a Grados
    3. Salir''')
    opcion = int(input('Elige una opción: '))

    if opcion == 1:
        print(f'El resultado de Grados a Fahrenheit es: {grados_fahren(pedir_datos()):.2f}')
    elif opcion == 2:
        print(f'El resultado de Fahrenheit a Grados es: {fahren_grados(pedir_datos()):.2f}')
    elif opcion == 3:
        print('Saliendo..')
        break
    else:
        print('Elige una opción válida.')