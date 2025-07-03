print('*** Operadores de Asignacion')
numero = 5
print(f'Valor de numero: {numero}')
numero = 10
print(f'Nuevo valor de numero: {numero}')

cadena = 'Saludos desde Python'
print(f'Valor de la cadena: {cadena}')
# Asignación múltiple
valor1, valor2, valor3 = 20, 'Aritz', False

print(f'''
Valor 1: {valor1}
Valor 2: {valor2}
Valor 3: {valor3}''')

# Asignación encadenada

contador1 = contador2 = 10

print(f'''
Valor contador 1: {contador1}
Valor contador 2: {contador2}''')

# Intercambio de valores en una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniciales x = {x}, y = {y}')
# Aplicando el concepto de asignación múltiple, intercambiamos valores
x, y = y, x

print(f'Invertir los valores x = {x}, y = {y}')

# Recibir múltiples valores de la entrada del usuario
nombre, apellido = input('Ingresa tu nombre y apeliidos separados por coma: ').split(',')
print(f'''
Nombre: {nombre.strip()}
Apellido: {apellido.strip()}''')