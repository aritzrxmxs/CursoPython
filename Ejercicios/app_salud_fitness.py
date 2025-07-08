print('*** Salud y Fitness ***')

# Constantes
META_PASOS_DIARIO = 10000
CALORIAS_POR_PASO = 0.04

# Pedimos valores al usuario
user_name = input('Introduce tu nombre: ')
steps_day = int(input('Pasos camidos en el día: '))

# Operamos
calorias_quemadas = steps_day * CALORIAS_POR_PASO
objetivo_complido = 'Si' if steps_day >= META_PASOS_DIARIO else 'No'

# Imprimimos
print(f'''
Nombre: {user_name}
Pasos caminados hoy: {steps_day}
Calorias quemadas: {calorias_quemadas:.1f} kcal
¿Has llegado al objetivo de 10k pasos?: {objetivo_complido}''')