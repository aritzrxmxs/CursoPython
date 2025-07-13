print('*** Agenda contactos ***')

agenda = {
    'Carlos': {
        'telefono': '664244539',
        'email': 'aritz@gmail.com',
        'direccion': 'Avellana, 7'
    },
    'Victoria': {
        'telefono': '652358974',
        'email': 'victoria@gmail.com',
        'direccion': 'calle sin numero'
    },
    'Pedro': {
        'telefono': '631268975',
        'email': 'pedro@gmail.com',
        'direccion': 'Plaza mayor 789'
    }
}

print(agenda)

# Acceder a la información de un contacto en especifico
print(f'''Informacion del contacto de Maria:
Telefono: {agenda['Victoria']['telefono']}
Email: {agenda.get('Victoria').get('email')}
Dirección: {agenda['Victoria']['direccion']}''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '665955632',
    'email': 'ana@mail.com',
    'direccion': 'calle dos tres'
}


print(agenda)

# Eliminar un contacto existente
agenda.pop('Carlos')
del agenda['Pedro']
print(agenda)

# Mostrar lo que queda

print('|nContactos en la agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}''')