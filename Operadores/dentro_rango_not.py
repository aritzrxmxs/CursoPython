# Resisar si una variable se encuentra dentro de rango entre 1 y 10
dato = int(input('Proporciona un dato entero: '))

# Revisamos si está dentro de rango
# esta_dentro_rango = 1 <= dato <= 10
# print(f'variable está dentro de rango (entre 1 y 10)? : {esta_dentro_rango}')

# Revisamos la logica inversa, si el dato está fuera de rango
esta_fuera_rango = not(1 <= dato <= 10)
print(f'Variable está fuera de rango (entre 1 y 10)? : {esta_fuera_rango}')