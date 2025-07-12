print('*** Lista de suscriptores ***')

suscriptores = {'aritz@mail.com', 'victoria@mail.com', 'carlos@mail.com'}



# Verificar si un nuevo suscriptor ya esta

nuevo_suscriptor = 'raul@mail.com'

if nuevo_suscriptor in suscriptores:
    print('El nuevo suscriptor ya está en la lista')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'Se ha agregado correctamente \'{nuevo_suscriptor}\'')
print(f'Lista de suscriptores: {suscriptores}')

# Eliminamos un suscriptor

suscriptor_eliminar = 'aritz@mail.com'
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} se ha eliminado.')
print(f'Lista de suscriptores: {suscriptores}')

# Verificar la cantidad total de suscriptores

print(f'Cantidad total: {len(suscriptores)}')

# Mostrar todos los suscriptores
print('--- Lista de suscriptores ---')
for elemento in suscriptores:
    print(elemento)