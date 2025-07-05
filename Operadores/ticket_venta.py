print('*** Generación ticket de venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio plátanos: '))
porcentaje_descuento = int(input('Introduce el descuento que quieres aplicar %: '))

# Calculo de subtotal
subtotal = precio_platanos + precio_pan + precio_leche +precio_lechuga

# Descuento

descuento = subtotal * (porcentaje_descuento/100)

# Subtotal con descuento

subtotal_descuento = subtotal - descuento

# Calculo con impuestos 21%
impuesto = subtotal_descuento * 0.21

# Calculamos el total con impuestos

coste_total = subtotal_descuento + impuesto

print(f'''
Subtotal: {subtotal:.2f}€
Descuento: {descuento} ({porcentaje_descuento}%)
Subtotal con descuento: {subtotal_descuento}€
Impuesto (21%): {impuesto:.2f}€
Precio total de compra: {coste_total:.2f}€
''')