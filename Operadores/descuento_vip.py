print('*** Sistema Descuentos VIP ***')
NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cuantos productos compraste hoy? '))
tiene_membresia = input('Tienes la membresia de la tienda (Si/No)? ')
es_elegible_descuento = ((cantidad_productos >= NO_PRODUCTOS_DESCUENTO)
                         and tiene_membresia.strip().lower() == 'si')
print(f'Tienes derecho a descuento?: {es_elegible_descuento}')