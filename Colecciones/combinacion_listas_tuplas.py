print('*** Combinacion de listas y tuplas ***')

# Definir una lista que almacena tuplas de productos

productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Pantalón', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# Imprimir la informacion de cada producto
# y ademas calculamos el precio total

precio_total = 0

print('Informacion de los productos: ')
for producto in productos:
     id, descripcion, precio = producto #unpacking
     print(f'ID: {id}')
     print(f'Descipción: {descripcion}')
     print(f'Precio: {precio}\n')
     # precio_total += precio
     precio_total += producto[2]

print(f'Precio total: {precio_total}')