print('*** Ejemplos sets ***')

# Crear un set

mi_set = {1, 2, 3, 4, 5, 5}

print(f'Set primero: {mi_set}')

# Agregar elementos al set

mi_set.add(6)
mi_set.add(7)
print(f'Set modificado: {mi_set}')

# Eliminar un elemento del conjunto

mi_set.remove(7)
print(f'eliminamos el 7: {mi_set}')

# Iterar los elementos

for elemento in mi_set:
    print(elemento, end = ' ')

# Comprobar si existe un elemento en el set
print(f'\nExiste el valor de 4 en el set?: {'Si' if 7 in mi_set else 'No'}')

# Objetener la longitud del set

print(f'Longitud del set: {len(mi_set)}')
