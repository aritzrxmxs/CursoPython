print('*** Suma acumulativa ***')
contador = 1
suma = 0
MAXIMO = 5

while contador <= MAXIMO:
    # Imprimir lo que se va a sumar
    print(f'Suma + contador: {suma} + {contador}')
    suma += contador
    contador += 1
    print(suma)
