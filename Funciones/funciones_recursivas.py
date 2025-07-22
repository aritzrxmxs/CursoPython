print('*** Imprimir del 1 al 5 de forma recursiva ***')

# Funcion recursiva

def funcion_resursiva(numero):
    if numero == 1:
        print(numero, end=' ')
    else:
        funcion_resursiva(numero - 1)
        print(numero, end=' ')

funcion_resursiva(5)