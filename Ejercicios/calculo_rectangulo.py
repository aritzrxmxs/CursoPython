print('*** Cálculo Área y Perímetro de un rectángulo ***')

DOBLE = 2

base = float(input('Introduce la base de tu rectángulo: '))
altura = float(input('Introduce la altura de tu rectángulo: '))

area = base * altura
perimetro = DOBLE * (base + altura)

print(f'''
El área del rectángulo es: {area:.2f}.
El perímetro del rectángulo es: {perimetro:.2f}.
''')