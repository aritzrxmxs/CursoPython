# Declaro las constantes

USER = 'Aritz'
PASSWORD = '1234'

# Empiezo a pedir valores
print('*** Sistema de autentificación ***')
nombre = input('Introduce el nombre: ')
contrasenia = input('Introduce la contraseña: ')

if nombre == USER and contrasenia == PASSWORD:
    print('¡¡Bienvenido al sistema!!')
elif not nombre == USER and contrasenia == PASSWORD:
    print('Usuario inválido.')
elif nombre == USER and not contrasenia == PASSWORD:
    print('Password inválido.')
else:
    print('Usuario y password inválidos.')