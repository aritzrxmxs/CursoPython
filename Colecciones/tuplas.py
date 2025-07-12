print('*** Manejo de Tuple')

mi_tuple = (1, 2, 3, 4, 5)
print(mi_tuple)

# iterar los elementos de una tupla

for elemento in mi_tuple:
    print(elemento, end = ' ')

# Crear una tupla para una coordenada x,y
coordenadas = (3, 5)

# Accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordenada en el eje y: {coordenadas[1]}')

# Crear tupla unitaria
tuple_one_element = 10,
print(tuple_one_element)

# tupla anidada
tupla_anidada = (1, (2,3), (4,5))
print(f'Segundo elemento tupla anidada: {tupla_anidada[1][0]}') # Posicion 1 (son 2,3) saco la "0" que es (2)