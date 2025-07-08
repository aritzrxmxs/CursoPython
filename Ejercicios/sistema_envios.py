# Voy a declarar las constantes primero

TARIFA_NACIONAL = 10 # Por kg
TARIFA_INTERNACIONAL = 20 # Por kg

# Voy a solicitar los valor, para saber que tarifa coge voy a usar numeros
print('*** CORREOS ***')
destino = int(input('Elige un destino (Nacional 1, Internacinal 2): '))
peso = float(input('Introduce el peso del paquete: '))

# Aqui opero para que quede bonito con los valores que he introducido.
tarifa = TARIFA_NACIONAL if destino == 1 else TARIFA_INTERNACIONAL
nombre_destino = 'Nacional' if destino == 1 else 'Internacional'

# Imprimimos los detalles
if destino == 1 or destino == 2:
    print('\n------ Detalles del pedido ------')
    print(f'Destino: {nombre_destino}.')
    print(f'Peso del paquete: {peso}kg.')
    print(f'Coste de {tarifa}€/kg.')
    print(f'Total pedido: {peso * tarifa}')
else:
    print('Introduce un valor valido.')
