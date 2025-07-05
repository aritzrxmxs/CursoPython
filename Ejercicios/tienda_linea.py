print('*** Tienda online ***')
# Condición
VALOR_MINIMO = 1000
valor_compra = float(input('Introduce el valor de tu compra: '))
miembro = input('¿Eres miembro de la tienda? (Si/No): ')
total_compra = None
if valor_compra >= VALOR_MINIMO and miembro.strip().lower() == 'si':
    descuento = valor_compra * 0.10
    total_compra = valor_compra - descuento
    print(f'''
Tu compra es de {valor_compra}€.
Tu descuento es de {descuento}€ (10%).
El total de tu compra es de {total_compra}€.
''')
elif miembro.strip().lower() == 'si':
    descuento = valor_compra * 0.05
    total_compra = valor_compra - descuento
    print(f'''
Tu compra es de {valor_compra}€.
Tu descuento es de {descuento}€ (5%).
El total de tu compra es de {total_compra}€.
''')
else:
    print(f'''
No tienes derecho a descuento.
El total de tu compra es de {valor_compra}€.
''')
