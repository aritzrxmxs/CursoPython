print('*** Sistema de Inventarios ***')
cantidad = int(input('Cuantos productos deseas agregar?: '))
almacen = []
for indice in range(cantidad):
    print(f'Proporciona los valores del producto {indice + 1}')
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))

    almacen.append({
        'id': indice,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
print('\n¡Valores añadidos correctamente!')

print(almacen)
#for indice in almacen:
 #   print(f'''--- Detalles del articulo {indice + 1} ---
  #  Nombre: {almacen[0].get('nombre')}
   # Precio: {almacen[0].get('precio')}
    #Cantidad: {almacen[0].get('cantidad')}
#''')
id = int(input('Introduce el ID del producto a buscar: '))

for indice, producto in enumerate(almacen):
    if id == producto.get('id'):
        print(f'''
        Id: {almacen[indice].get('id')}
            Nombre: {almacen[indice].get('nombre')}
            Precio: {almacen[indice].get('precio')}
            Cantidad: {almacen[indice].get('cantidad')}
        ''')
    else:
        print('El producto seleccionado no existe.')
print('---- Detalles del almacén ----\n')
for producto in almacen:
    print(f'''
    -------------------------------------   
    Id: {producto.get('id')}
        Nombre: {producto.get('nombre')}
        Precio: {producto.get('precio')}
        Cantidad: {producto.get('cantidad')}
    -------------------------------------\n
    ''')