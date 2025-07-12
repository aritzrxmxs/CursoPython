print('*** Playlist de canciones ***')

# Definimos una lista vacía
lista_canciones = []

numero_canciones = int(input('Cuantas canciones quieres agregar: '))

# iteramos cada elemento de la lista paraa gregar un nuevo elemento

for indice in range(numero_canciones):
    cancion = input(f'Introduce la cancion {indice + 1}: ')
    lista_canciones.append(cancion)

# Ordenar la lista en orden alfabético con .sort

lista_canciones.sort()

# Mostrar el playlist

print(f'\n Lista de reproduccion en orden alfabetico: ')
print(lista_canciones)

print('Iteramos la playlist')
lista_canciones.sort(reverse=True)
for canciones in lista_canciones:
    print(f'- {canciones}')