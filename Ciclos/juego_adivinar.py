from random import randint

numero = randint(1, 50)
salir = False
contador = 5
print('*** ADIVINA EL NUMERO ***')
while not salir:
    if contador > 0:
        seleccion = int(input('Introduce un número del 1 al 50: '))
        if seleccion >= 1 and seleccion <= 50:
            if seleccion != numero:
                if seleccion > numero:
                    contador -= 1
                    if contador > 0:
                        print(f'CASI!! El numero es menor. Te quedan {contador} intentos.')

                else:
                    contador -= 1
                    if contador > 0:
                        print(f'CASI!! El número es mayor. Te quedan {contador} intentos')

            else:
                print(f'¡¡ENHORABUENA!! Acertaste el número en {contador} intentos.')
                salir = True
        else:
            print('Elige una opción válida dentro del rango.')
    else:
        print('¡¡Se acabaron los intentos!!')
        salir = True
