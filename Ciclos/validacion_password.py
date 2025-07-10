
password = input('Introduce la contraseña: ')
while len(password) < 6:
    print('No cumple los requisitos. Mínimo 6 carácteres.')
    password = input('Introduce de nueva una contraseña: ')
else:
    print('El valor es correcto.')