print('*** Imprimir detalles de una persona con kwargs ***')

# Funcion que acepta argumentos variables en forma de llave/valor o dict
def imprimir_detalle(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}:{valor}')

# Llamamos a la funcion
imprimir_detalle(nombre='Aritz', edad=30, ciudad='Sevilla')
imprimir_detalle(nombre='Victoria', edad=29, ciudad='Sevilla', empresa='Orange')