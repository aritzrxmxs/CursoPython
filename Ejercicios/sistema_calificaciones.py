print('*** Sistema calificaciones ***')

nota = float(input('Introduce tu nota de 0 a 10: '))
letra = None
correcto = True
if nota >= 9 and nota <= 10:
    letra = 'A'
elif nota >= 8 and nota <= 9:
    letra = 'B'
elif nota >= 7 and nota <= 8:
    letra = 'C'
elif nota >= 6 and nota <= 7:
    letra = 'D'
elif nota >= 0 and nota <= 6:
    letra = 'F'
else:
    print('Valor desconocido. Introduce un valor valido.')
    correcto = False

if correcto:
    print(f'El valor de tu nota ({nota}) es: {letra}')