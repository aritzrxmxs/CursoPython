NOMBRE_CORRECTO = 'admin'
CONTRASEÑA_CORRECTA = '1234'

print('*** Sistema Autentificación ***')

nombre_user = input('User: ')
password = input('Password: ')

is_true = (nombre_user.strip() == NOMBRE_CORRECTO
           and password.strip() == CONTRASEÑA_CORRECTA)

print(f'Datos correstos: {is_true}')
