print('*** Suma argumentos variables ***')

# Fucion sumar que acepta argumentos variables

def sumar(*args):
    total=0
    for numero in args:
        total += numero
    return total
print(f'Total: {sumar(1,2,3,4,5)}')