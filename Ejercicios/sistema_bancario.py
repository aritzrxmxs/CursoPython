print('*** Bienvenidos al sistma bancario ***')

salir_sistema_txt = input('Deseas salir del sistema (Si/No)? ')
salir_sistema = salir_sistema_txt.strip().lower() == 'Si'

if not salir_sistema:
    print('Continuamos dentro del sistema')
else:
    print('Salimos del sistema')