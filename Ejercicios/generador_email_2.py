nombre_usuario = input('Introduce tu nombre: ')
apellidos_usuario = input('Introduce tus apellidos: ')
nombre_empresa = input('Introduce el nombre de tu empresa: ')
extension = input('Introduce la extensión de dominio: ')

# Normalizar los valores recibidos
usuario_cambiado = nombre_usuario.strip().lower().replace(' ','.')
apellidos_cambiado = apellidos_usuario.strip().lower().replace(' ','.')
empresa_cambiado = nombre_empresa.strip().lower().replace(' ','')
extension_cambiado = extension.strip().lower().replace(' ','')

email = f'{usuario_cambiado}.{apellidos_cambiado}@{empresa_cambiado}{extension_cambiado}'
print(email)