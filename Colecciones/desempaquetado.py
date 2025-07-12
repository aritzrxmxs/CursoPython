print('*** unpacking ***')

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado

id, descipcion, precio = producto

# imprimimos
print(f'Tupla completa: {producto}')

# valores inmdependientes

print(f'''
id: {id}
Descripcion: {descipcion}
Precio: {precio}''')