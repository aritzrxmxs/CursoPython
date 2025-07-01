# Ejercicio de generador de email

# Nombre completo del usuario
nombre_usuario = ' Aritz Ramos Lozares '
nombre_empresa = 'Global Mentoring'
dominio = '.com'

usuario_normalizado = nombre_usuario.strip().replace(' ', '.').lower()
empresa_normalizada = nombre_empresa.replace(' ', '').lower()
email = f'{usuario_normalizado}@{empresa_normalizada}{dominio}'
print('*** generador de Email ***')
print(f'Nombre usuario: {nombre_usuario}')
print(f'Nombre usuario normalizado: {usuario_normalizado}')
print()
print(f'Nombre empresa: {nombre_empresa}')
print(f'Extensión del dominio: {dominio}')
print(f'Dominio de email normalizado: @{empresa_normalizada}{dominio}')
print()
print(f'Email final generado: {email}')