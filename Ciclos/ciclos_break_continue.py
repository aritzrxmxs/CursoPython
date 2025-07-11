print('Break y continue')

# Ejemplo break
print('break')
for numero in range(1, 10):
    if numero % 2 == 0:
        print(f'{numero}')
        break  # Salimos del ciclo

# Ejemplo Continue
print('Continue')
for numero in range(1, 10):
    if numero % 2 == 1:
        continue
    print(numero)
