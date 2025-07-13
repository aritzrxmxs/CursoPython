print('*** Lista de suscriptores ***')
# Definimos el set inicial

# suscriptores = {} # aqui se define un diccionario vacío
suscriptores = set()

numero_suscriptores = int(input('Di el numero de suscriptores: '))

for _ in range(numero_suscriptores):
    suscriptores.add(input('Nuevo suscriptor(email): '))



# Verificar si un nuevo suscriptor ya esta

nuevo_suscriptor = input('Proporciona el nuevo suscriptor: ')

if nuevo_suscriptor in suscriptores:
    print('El nuevo suscriptor ya está en la lista')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'Se ha agregado correctamente \'{nuevo_suscriptor}\'')
print(f'Lista de suscriptores: {suscriptores}')

# Eliminamos un suscriptor

suscriptor_eliminar = input('Proporciona un suscriptor a eliminar: ')
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} se ha eliminado.')
print(f'Lista de suscriptores: {suscriptores}')

# Verificar la cantidad total de suscriptores

print(f'Cantidad total: {len(suscriptores)}')

# Mostrar todos los suscriptores
print('--- Lista de suscriptores ---')
for elemento in suscriptores:
    print(elemento)