inventario = [
        {'id': 1, 'nombre': 'Camisa', 'precio': 25.99, 'cantidad': 50},
        {'id': 2, 'nombre': 'Pantalones', 'precio': 39.99, 'cantidad': 30},
        {'id': 3, 'nombre': 'Zapatos', 'precio': 49.99, 'cantidad': 20}
    ]

def menu_texto():
    print('''
    --- Menú ---
        1. Mostrar inventario
        2. Agregar nuevo producto
        3. Buscar producto por Id
        4. Salir''')

def mostrar_inventario():
    print('--- INVENTARIO ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f' Precio: {producto.get('precio')}, Cantidad: {producto.get('cantidad')}')

def agregar_producto():
    print('--- Agregar nuevo producto ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    nuevo_producto = {'id': id, 'nombre': nombre, 'precio': precio,
                      'cantidad': cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado con exito!!')

def buscar_por_id():
    id_buscar = int(input('Introduce el ID a buscar: '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
                  f' Precio: {producto.get('precio')}, '
                  f'Cantidad: {producto.get('cantidad')}')
            return

    print('El ID proporcionado no existe.')
end = False

while not end:
    menu_texto()
    menu = int(input('\tProporciona una opción (1-4): '))

    if menu == 1:
        mostrar_inventario()
    elif menu == 2:
        agregar_producto()
    elif menu == 3:
        buscar_por_id()
    elif menu == 4:
        print('Saliendo del programa..')
        end = True
    else:
        print('\tIntroduce una opción válida..')
