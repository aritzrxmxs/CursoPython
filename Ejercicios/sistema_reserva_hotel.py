# Declaro las constantes primero

CUARTO_SIN_VISTAS = 150.50 # Por día
CUARTO_CON_VISTAS = 190.50 # Por día

# Pedimos los datos
print('*** Sistema de Reserva de Hotel ***')
nombre_cliente = input('Nombre: ')
dias_estancia = int(input('Días de estancia: '))
cuarto_con_vistas = input('¿Cuarto con vistas al mar? (Si/No): ')

# Voy a declarar una variable ya con el True o False de si quiere una habitacion
# con vistas.

con_vistas = CUARTO_CON_VISTAS if cuarto_con_vistas.strip().lower() == 'si' else CUARTO_SIN_VISTAS

print(f'''
------ Detalles de la reserva ------
Nombre: {nombre_cliente}
Días de estancia: {dias_estancia}
¿Quiere vistas al mar?: {cuarto_con_vistas.upper()}
Precio por noche: {con_vistas}€
Total reserva: {dias_estancia * con_vistas:.2f}€''')