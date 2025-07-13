print('*** Diccionarios en Python ***')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Aritz',
    'edad': 29,
    'ciudad': 'Sevilla'
}

print(f'Diccionario de persona: {persona}')

# Accedeer a los elementos del diccionario

print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Ciudad: {persona.get('ciudad')}')

# Modificar un valor del diccionario
persona['edad'] = 35
print(f'Diccionario persona: {persona}')

# gregar u nuevo elemento
persona['profesion'] = 'Programador'
print(f'Diccionario persona: {persona}')

# Eliminar un elemento
del persona['ciudad']
print(f'Diccionario persona: {persona}')

persona.pop('profesion')
print(f'Diccionario persona: {persona}')

# Iterar los elementos de un dict (llave, valor)

for llave, valor in persona.items():
    print(f'{llave}: {valor}')

# Obtener los valores
for valor in persona.values():
    print(f'-Valor: {valor}')

# Obtener llaves

for llaves in persona.keys():
    print(f'-Llaves: {llaves}')