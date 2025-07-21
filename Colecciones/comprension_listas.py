print('*** COmprension de listas ***')

numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x  in numeros]
print(cuadrados)

# Listas numeros pares

numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0]
print(pares)

# Lista salñudando a cada nombre

nombres = ['Aritz', 'Victoria', 'Raul']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)