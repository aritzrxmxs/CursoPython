print('*** Máquina de Scancks ***')

maquina = [
    {'id': 1, 'nombre': 'Patatas', 'precio': 1.50},
    {'id': 2, 'nombre': 'Refresco', 'precio': 3.20},
    {'id': 3, 'nombre': 'Sandwich', 'precio': 4.25}
]
compra = []

def menu_texto():
    print('''
Menú:
    1. Mostrar Snacks
    2. Comprar Snack
    3. Mostrar Ticket
    4. Salir''')

def mostrar_snacks():
    print('\n--- SNACKS DISPONIBLES ---')
    for snack in maquina:
        print(f'\tID: {snack.get('id')} -> {snack.get('nombre')} - '
              f'{snack.get('precio'):.2f}€')

def comprar_snack():
    print('\n--- COMPRAR SNACK ---')
    id_buscar = int(input('Introduce el ID del snack: '))
    for snack in maquina:
        if snack.get('id') == id_buscar:
            compra.append(snack)
            print('Producto agregado a la cesta.')
            return
    print('ID de Snack no encontrado.')

def mostrar_ticket():
    total = 0
    print('\n--- Ticket de Compra ---\n')
    for snack in compra:
        print(f'\t{snack.get('nombre')} - '
              f'{snack.get('precio'):.2f}€')
        total += snack.get('precio')
    print(f'\n\tPrecio total de compra: {total:.2f}€')
while True:
    menu_texto()
    opcion = int(input('\tIntroduce una opción: '))

    if opcion == 1:
        mostrar_snacks()
    elif opcion == 2:

        comprar_snack()
    elif opcion == 3:
        mostrar_ticket()
    elif opcion == 4:
        print('Saliendo del programa..')
        break
    else:
        print('Introduce una opción válida..')

