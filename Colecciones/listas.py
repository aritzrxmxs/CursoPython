print('*** Manejo de listas ***')

lista = [1, 2, 3, 4, 5]

print(f'{lista} -- lista original')


# Largo de una lista

print(f'Largo de la lista: {len(lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {lista[-1]}')

# Modificar los elementos de una lista
lista[1] = 10
print(f'Modificamos el valor del indice 1: {lista[1]}')

# Agregamos un nuevo elemento al final de la lista
lista.append(6)
print(f'Se agrego el elemento 6 al final: {lista}')

# Añadir un nuevo elemento en un índice especifico

lista.insert(2, 'Hola')
print(f'Añadí Hola en el indice 2: {lista}')

# Eliminar elementos de una lista

# Metodo remove

lista.remove('Hola')
print(f'Eliminamos el texto: {lista}')

# Eliminamos por indice con el metodo pop
lista.pop(0)
print(f'Eliminamos el indice 1 de la lista: {lista}')

# Eliminar usando la palabra del
del lista[2]
print(f'Eliminamos el elemento del indice 2 (4): {lista}')

# Obtener sublistas

sublista = lista[1:3]

print(sublista)