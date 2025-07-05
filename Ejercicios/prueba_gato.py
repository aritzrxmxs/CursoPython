VALIDO = 'Victoria'

nombre = input('Introduce tu nombre: ')

if nombre.lower() == VALIDO.lower():
    print('Eres un gatito lindo.')
else:
    print('Eres una araña fea.')