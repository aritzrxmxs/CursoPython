print('*** Identifica la estación del año ***')

month = int(input('Choose a number of month (1-12): '))

if month in (1,2,12):
    print('Invierno')
elif month in (3,4,5):
    print('Primavera')
elif month in (6,7,8):
    print('Verano')
elif month in (9,10,11):
    print('Otoño')
else:
    print('Estación desocnocida.')