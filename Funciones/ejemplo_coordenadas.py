print('*** Obtener coordenadas x, y, z ***')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return (x, y, z)
# Llamar a la funcion

print(f'{obtener_coordenadas()}')

# Unpacking

x1, y1, z1 = obtener_coordenadas()

print(f'X = {x1}, Y = {y1}, Z = {z1}')