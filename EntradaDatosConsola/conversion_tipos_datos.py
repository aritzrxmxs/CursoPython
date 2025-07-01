# Conversión de tipos de datos

# Convertir de cadena a numero

numero_cadena = '10'
numero_entero = int(numero_cadena)
print(f'Valor numérico en cadena: {numero_cadena}')
print(f'Cadena a entero: {numero_entero}')

# Convertir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante: {numero_flotante}')

# Convertir de numero a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Numero a cadena: {numero_cadena}')

# Convertir a booleano
# Tipo bool es False en los siguientes casos
# Si el valor es 0, cadena vacía, o None, entonces es False
# Es verdadero, si el valor es distinto de 0, si es distinto de cadena vacía
# y si es distinto de None
numero_entero = 1
booleano = bool(numero_entero)
print(f'Valor booleano de 0: {booleano}') # False, incluye 0, 0.0

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5: {booleano}') # True

cadena = '' # El largo de la cadena es 0 por eso es False. Se aplica a colecciones vacías
booleano = bool(cadena)
print(f'Valor booleano de una cadena vacía: {booleano}')


cadena = 'Cadena con valor'
booleano = bool(cadena)
print(f'Valor booleano de una cadena NO vacía: {booleano}') # True

variable = None
booleano = bool(variable)
print(F'Valor booleano de None: {booleano}')