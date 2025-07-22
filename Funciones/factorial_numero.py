print('*** Factorial del número 5 ***')

def factorial_recursiva(numero):
    # Caso base, factorial de 0! = 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es: 1')
        return 1
    else: # Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resultado factorial parcial {numero} es: {factorial_parcial}')
        return factorial_parcial

numero = 5
resultado = factorial_recursiva(numero)
print(f'El factorial de {numero} es: {resultado}')